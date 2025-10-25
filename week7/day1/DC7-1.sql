-- Re-create sample table (safe rerun)
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

-- Insert 20 sample records
INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

-- 1.1 Detect NULL or blank values
SELECT *
FROM employees
WHERE employee_name IS NULL OR TRIM(employee_name) = ''
   OR salary IS NULL
   OR hire_date IS NULL OR TRIM(hire_date) = ''
   OR department IS NULL OR TRIM(department) = '';

-- 1.2 Handle NULL department (simple imputation to 'Unknown')
UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL OR TRIM(department) = '';


-- 2.1 Find logical duplicates (case/space-insensitive)
WITH norm AS (
  SELECT
    employee_id,
    LOWER(REGEXP_REPLACE(employee_name, '\s+', ' ', 'g')) AS nm,
    hire_date,
    LOWER(department) AS dept
  FROM employees
)
SELECT n1.*
FROM norm n1
JOIN norm n2
  ON n1.employee_id <> n2.employee_id
 AND n1.nm   = n2.nm
 AND n1.hire_date = n2.hire_date
 AND n1.dept = n2.dept
LIMIT 20;

-- 2.2 Remove logical duplicates keeping the smallest employee_id
WITH ranked AS (
  SELECT
    employee_id,
    ROW_NUMBER() OVER (
      PARTITION BY
        LOWER(REGEXP_REPLACE(employee_name, '\s+', ' ', 'g')),
        hire_date,
        LOWER(department)
      ORDER BY employee_id
    ) AS rn
  FROM employees
)
DELETE FROM employees e
USING ranked r
WHERE e.employee_id = r.employee_id
  AND r.rn > 1;

-- 3.1 Standardize employee_name to Title Case, trim spaces
UPDATE employees
SET employee_name = INITCAP(TRIM(employee_name));

-- 3.2 Standardize department names (Title Case), trim spaces
UPDATE employees
SET department = INITCAP(TRIM(department));


-- 4.1 Validate parsable dates first (optional check)
SELECT employee_id, hire_date
FROM employees
WHERE TO_DATE(hire_date, 'YYYY-MM-DD') IS NULL;  -- should be none with given data

-- 4.2 Convert the column type from VARCHAR to DATE
ALTER TABLE employees
  ALTER COLUMN hire_date TYPE DATE
  USING TO_DATE(hire_date, 'YYYY-MM-DD');


-- 5.1 Detect salary outliers using IQR method
WITH q AS (
  SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) AS q3
  FROM employees
),
bounds AS (
  SELECT
    q1, q3,
    (q3 - q1) AS iqr,
    (q1 - 1.5*(q3 - q1)) AS lower_bound,
    (q3 + 1.5*(q3 - q1)) AS upper_bound
  FROM q
)
SELECT e.*
FROM employees e, bounds b
WHERE e.salary < b.lower_bound OR e.salary > b.upper_bound;


-- 6.1 Trim again to be safe after transformations
UPDATE employees
SET employee_name = TRIM(employee_name),
    department    = TRIM(department);

-- 6.2 Optional: normalize department to a small domain (dictionary)
-- Example: map synonyms (if any) into a canonical set
UPDATE employees
SET department = 'Human Resources'
WHERE department = 'Hr';

-- 6.3 Optional: scale salary to thousands (for reporting) into a new column
ALTER TABLE employees DROP COLUMN IF EXISTS salary_k;
ALTER TABLE employees ADD COLUMN salary_k NUMERIC(10,2);
UPDATE employees SET salary_k = ROUND(salary/1000.0, 2);

