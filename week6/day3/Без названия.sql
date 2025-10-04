--ON UPDATE, ON DELETE OPTIONS

-- PARENT TABLE
CREATE TABLE colors (
color_id SERIAL PRIMARY KEY,
color_name VARCHAR (15)
)

INSERT INTO colors (color_name)
VALUES ('black'), ('grey'), ('red')

SELECT * FROM colors

-- CHILD TABLE WITH THE OPTION "ON DELETE RESTRICT"
CREATE TABLE cars_ondelete (
car_id SERIAL PRIMARY KEY,
car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT,
car_name TEXT
)

INSERT INTO cars_ondelete (car_color, car_name)
VALUES
((SELECT color_id FROM colors WHERE color_name = 'black'), 'Mazda'),
((SELECT color_id FROM colors WHERE color_name = 'red'), 'BMW'),
((SELECT color_id FROM colors WHERE color_name = 'grey'), 'Ferrari')

DELETE FROM colors WHERE color_id = 1
-- ERROR:  update or delete on table "colors" violates foreign key constraint "cars_ondelete_car_color_fkey" on table "cars_ondelete"
-- Key (color_id)=(1) is still referenced from table "cars_ondelete". 

CREATE TABLE cars_casckare (
car_id SERIAL PRIMARY KEY,
car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT,
car_name TEXT)

INSERT INTO cars_casckare (car_color, car_name)
VALUES
((SELECT color_id FROM colors WHERE color_name = 'black'), 'Mazda'),
((SELECT color_id FROM colors WHERE color_name = 'red'), 'BMW'),
((SELECT color_id FROM colors WHERE color_name = 'grey'), 'Ferrari')

SELECT * FROM colors


CREATE TABLE cars_null (
car_id SERIAL PRIMARY KEY,
car_color INTEGER REFERENCES colors (color_id) ON DELETE SET NULL,
car_name TEXT)

INSERT INTO cars_null (car_color, car_name)
VALUES
((SELECT color_id FROM colors WHERE color_name = 'black'), 'Mazda'),
((SELECT color_id FROM colors WHERE color_name = 'red'), 'BMW'),
((SELECT color_id FROM colors WHERE color_name = 'grey'), 'Ferrari')

SELECT * FROM cars_null

DELETE FROM colors WHERE color_id = 3
