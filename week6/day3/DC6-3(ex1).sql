-- Instructions
-- You are going to practice tables relationships

-- Part I

-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)
CREATE TABLE customer(
customer_id SERIAL NOT NULL,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(100) NOT NULL,
PRIMARY KEY (customer_id)
)

CREATE TABLE customer_profile(
profile_id SERIAL NOT NULL,
isLoggedIn BOOLEAN NOT NULL DEFAULT false,
customer_id INTEGER NOT NULL,
FOREIGN KEY (profile_id) REFERENCES customer (customer_id)
)
-- Insert those customers

-- John, Doe
-- Jerome, Lalu
-- Lea, Rive
INSERT INTO customer (first_name, last_name)
VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive')

-- Insert those customer profiles, use subqueries

-- John is loggedIn
-- Jerome is not logged in
INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES
(TRUE, (SELECT customer_id FROM customer WHERE first_name = 'John')),
(FALSE, (SELECT customer_id FROM customer WHERE first_name = 'Jerome'))

-- Use the relevant types of Joins to display:
SELECT * FROM customer AS c
LEFT JOIN customer_profile AS cp
ON c.customer_id = cp.customer_id

-- The first_name of the LoggedIn customers
SELECT first_name FROM customer AS c
INNER JOIN customer_profile AS cp
ON c.customer_id = cp.customer_id
WHERE isLoggedIn = TRUE

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
SELECT first_name, isLoggedIn FROM customer AS c
FULL JOIN customer_profile AS cp
ON c.customer_id = cp.customer_id

-- The number of customers that are not LoggedIn
SELECT COUNT(*) FROM customer AS c
INNER JOIN customer_profile AS cp
ON c.customer_id = cp.customer_id
WHERE isLoggedIn = FALSE
