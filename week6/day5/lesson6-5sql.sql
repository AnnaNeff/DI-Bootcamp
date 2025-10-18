CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);

CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
)

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200);

SELECT * FROM employees AS e
FULL JOIN sales_data AS s
ON e.employee_id = s.employee_id

SELECT e.employee_id, e.first_name, e.last_name, e.department_id, s.sales,
       RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS sales_rank,
       DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY s.sales DESC) AS dense_sales_rank
FROM employees e
JOIN sales_data s ON e.employee_id = s.employee_id;


SELECT employee_id, first_name, last_name, department_id, salary,
        RANK() OVER (PARTITION BY department_id ORDER BY salary) AS rank
FROM employees

SELECT employee_id, first_name, last_name, salary,
       DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dense_rank
FROM employees

SELECT employee_id, first_name, last_name, salary,
       NTILE(4) OVER (PARTITION BY department_id ORDER BY salary DESC) AS quartile
FROM employees

SELECT e.employee_id, e.first_name, e.last_name, s.sales,
       RANK() OVER (PARTITION BY department_id ORDER BY sales DESC) AS sales_rank
FROM employees AS e
FULL JOIN sales_data AS s
ON e.employee_id = s.employee_id

-- 1. Task: Use the ROW_NUMBER() function to list employees in each department, ordered by their salary in descending order. Display the department, employee name, and their salary rank within the department.

SELECT department_id, first_name, salary,
	ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary)
FROM employees

-- 2. Task: Calculate the cumulative salary for employees in each department using the SUM() function with windowing.
SELECT department_id, first_name, salary,
	SUM(salary) OVER (PARTITION BY department_id ORDER BY salary) AS cum_sum
FROM employees