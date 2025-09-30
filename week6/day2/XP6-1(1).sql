-- All items, ordered by price (lowest to highest).
SELECT * FROM items
ORDER BY price

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
SELECT * FROM items WHERE price >= 80
ORDER BY price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
SELECT c.first_name, c.last_name FROM customers AS c
ORDER BY c.first_name
LIMIT 3

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
SELECT c.last_name FROM customers AS c
ORDER BY c.last_name DESC