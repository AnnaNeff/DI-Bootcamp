-- Create a table called product_orders and a table called items. You decide which fields should be in each table, although make sure the items table has a column called price.
CREATE TABLE items(
item_id SERIAL NOT NULL,
item_name VARCHAR(100),
item_price INT NOT NULL,
PRIMARY KEY (item_id)
)

CREATE TABLE product_orders(
order_id INT NOT NULL,
item_id INT NOT NULL,
FOREIGN KEY (item_id) REFERENCES items(item_id)
)

INSERT INTO items(item_name, item_price)
VALUES
('Oranges', 20),
('Banana', 15),
('Milk', 7),
('Chiken', 50),
('Tomatos', 10)

INSERT INTO product_orders(order_id, item_id)
VALUES
(1, (SELECT item_id FROM items WHERE item_name = 'Oranges')),
(1, (SELECT item_id FROM items WHERE item_name = 'Banana')),
(1, (SELECT item_id FROM items WHERE item_name = 'Milk')),
(2, (SELECT item_id FROM items WHERE item_name = 'Milk')),
(2, (SELECT item_id FROM items WHERE item_name = 'Chiken')),
(2, (SELECT item_id FROM items WHERE item_name = 'Tomatos')),
(3, (SELECT item_id FROM items WHERE item_name = 'Milk')),
(3, (SELECT item_id FROM items WHERE item_name = 'Tomatos')),
(3, (SELECT item_id FROM items WHERE item_name = 'Banana'))

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.

-- Create a function that returns the total price for a given order.
SELECT order_id, SUM(item_price) FROM product_orders AS p
LEFT JOIN items AS i
ON p.item_id = i.item_id
WHERE order_id = 2
GROUP BY order_id


-- Bonus :
-- Create a table called users.
-- There should be a one to many relationship between the users table and the product_orders table.
-- Create a function that returns the total price for a given order of a given user.
CREATE TABLE users(
user_id INT NOT NULL,
user_name VARCHAR (100),
order_id INT
)

INSERT INTO users (user_id,user_name,order_id)
VALUES
(1, 'Anna Neff', 1),
(2, 'John Doe', 2),
(1, 'Anna Neff', 3)

SELECT p.order_id, SUM(item_price) FROM product_orders AS p
INNER JOIN items AS i
ON p.item_id = i.item_id
INNER JOIN users AS u
ON u.order_id = p.order_id
WHERE p.order_id = 3 AND user_id = 1
GROUP BY p.order_id


