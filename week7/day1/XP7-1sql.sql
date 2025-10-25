DROP TABLE IF EXISTS df_employee;
CREATE TABLE df_employee AS
SELECT
  -- unique identifier from employee_id + date (stored as text)
  s.employee_id || '_' || CAST(s.date AS TEXT) AS id,
  -- keep only the DATE part (SQLite DATE() trims timestamp)
  DATE(s.date) AS month_year,
  s.employee_id,
  e.employee_name,
  -- alias the gender right away (no renaming needed later)
  TRIM(e.gen_mf) AS gender,
  e.age,
  CAST(s.salary AS REAL) AS salary,
  f.function_group,
  c.company_name,
  c.company_city,
  c.company_state,
  c.company_type,
  c.const_site_category
FROM emp_dataset AS s
LEFT JOIN functions AS f  ON f.function_code  = s.func_code
LEFT JOIN companies AS c  ON c.company_name   = s.comp_name
LEFT JOIN employees AS e  ON e.employee_code_emp = s.employee_id;

-- 1) Quick look
SELECT * FROM df_employee;

-- 2) TRIM all text columns (remove leading/trailing spaces)
UPDATE df_employee
SET
  id                  = TRIM(id),
  employee_name       = TRIM(employee_name),
  gender              = TRIM(gender),
  function_group      = TRIM(function_group),
  company_name        = TRIM(company_name),
  company_city        = TRIM(company_city),
  company_state       = TRIM(company_state),
  company_type        = TRIM(company_type),
  const_site_category = TRIM(const_site_category);

-- 3) Check NULLs and empties (use TRIM='' for empty strings)
SELECT *
FROM df_employee
WHERE id IS NULL
   OR month_year IS NULL
   OR employee_id IS NULL
   OR employee_name IS NULL
   OR gender IS NULL
   OR age IS NULL
   OR salary IS NULL
   OR function_group IS NULL
   OR company_name IS NULL
   OR company_city IS NULL
   OR company_state IS NULL
   OR company_type IS NULL
   OR const_site_category IS NULL
   OR TRIM(id) = ''
   OR TRIM(employee_name) = ''
   OR TRIM(gender) = ''
   OR TRIM(function_group) = ''
   OR TRIM(company_name) = ''
   OR TRIM(company_city) = ''
   OR TRIM(company_state) = ''
   OR TRIM(company_type) = ''
   OR TRIM(const_site_category) = '';

-- 4) Delete rows with detected missing salary values (empty strings)
DELETE FROM df_employee
WHERE salary IS NULL
   OR (CAST(salary AS TEXT) = '')
   OR (TRIM(CAST(salary AS TEXT)) = '');


-- Latest month boundary
WITH last_m AS (
  SELECT MAX(month_year) AS last_month FROM df_employee
)
-- 3.1 Total current employees (distinct heads)
SELECT COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT last_month FROM last_m);

-- 3.2 Current employees by company (distinct heads)
WITH last_m AS (
  SELECT MAX(month_year) AS last_month FROM df_employee
)
SELECT
  company_name,
  COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT last_month FROM last_m)
GROUP BY company_name
ORDER BY employee_count DESC, company_name ASC;


-- 4.1 Employees per city (latest month) with percentage
WITH last_m AS (
  SELECT MAX(month_year) AS last_month FROM df_employee
),
city_cnt AS (
  SELECT company_city, COUNT(DISTINCT employee_id) AS cnt
  FROM df_employee
  WHERE month_year = (SELECT last_month FROM last_m)
  GROUP BY company_city
)
SELECT
  company_city,
  cnt AS employee_count,
  ROUND(100.0 * cnt / SUM(cnt) OVER (), 2) AS percentage
FROM city_cnt
ORDER BY employee_count DESC, company_city;

-- 4.2 Total employees each month (distinct heads)
SELECT
  DATE(month_year) AS pay_month,
  COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY DATE(month_year)
ORDER BY pay_month;

-- 4.3 Average employees per month (overall)
WITH monthly AS (
  SELECT DATE(month_year) AS pay_month,
         COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY DATE(month_year)
)
SELECT ROUND(AVG(employee_count), 2) AS avg_employees_per_month
FROM monthly;


-- 5.1 Min/Max employees across months and which months
WITH monthly AS (
  SELECT DATE(month_year) AS pay_month,
         COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY DATE(month_year)
)
SELECT pay_month, employee_count
FROM monthly
ORDER BY employee_count ASC, pay_month
LIMIT 1;

WITH monthly AS (
  SELECT DATE(month_year) AS pay_month,
         COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY DATE(month_year)
)
SELECT pay_month, employee_count
FROM monthly
ORDER BY employee_count DESC, pay_month
LIMIT 1;

-- 5.2 Monthly average number of employees by function group
WITH grp_month AS (
  SELECT
    function_group,
    DATE(month_year) AS pay_month,
    COUNT(DISTINCT employee_id) AS employee_count
  FROM df_employee
  GROUP BY function_group, DATE(month_year)
)
SELECT
  function_group,
  ROUND(AVG(employee_count), 2) AS avg_employees_per_month
FROM grp_month
GROUP BY function_group
ORDER BY avg_employees_per_month DESC, function_group;

-- 5.3 Annual average salary
SELECT
  SUBSTR(CAST(month_year AS TEXT), 1, 4) AS year,
  ROUND(AVG(CAST(salary AS REAL)), 2) AS average_salary
FROM df_employee
GROUP BY SUBSTR(CAST(month_year AS TEXT), 1, 4)
ORDER BY year;
