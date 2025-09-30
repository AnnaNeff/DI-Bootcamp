CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	item VARCHAR (50) NOT NULL,
	price INTEGER NOT NULL
	);

CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (100) NOT NULL
	)

INSERT INTO items(item, price)
	VALUES ('Small Desk', 100),
		('Large desk', 300),
		('Fan', 80)
		
INSERT INTO customers(first_name, last_name)
	VALUES ('Greg', 'Jones'),
		('Sandra', 'Jones'),
		('Scott', 'Scott'),
		('Trevor', 'Green'),
		('Melanie', 'Johnson')

SELECT * FROM items

SELECT * FROM customers

SELECT * FROM items WHERE price >80

SELECT * FROM items WHERE price < 300

SELECT * FROM customers WHERE last_name = ‘Smith’

-- Outcome: "ERROR:  column "‘smith’" does not exist"

SELECT * FROM customers WHERE last_name = 'Jones'

SELECT * FROM customers WHERE last_name != 'Scott'






