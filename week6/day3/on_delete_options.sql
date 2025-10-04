-- ON UPDATE, ON DELETE OPTIONS

--CREATING THE PARENT TABLE (COLORS)
-- CREATE TABLE colors (
-- color_id SERIAL PRIMARY KEY,
-- name VARCHAR(15)
-- );

-- INSERT INTO colors (name)
-- VALUES ('black'), ('grey'), ('red');

-- SELECT * FROM colors

--CREATING THE CHILD TABLE WITH THE OPTION "ON DELETE RESTRICT" WHICH IS THE DEFAULT 
-- CREATE TABLE cars_restrict(
-- car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT,
-- car_name TEXT);


-- INSERT INTO cars_restrict (car_color, car_name)
-- VALUES
-- ((SELECT color_id FROM colors WHERE name = 'black'),'Mazda'),
-- ((SELECT color_id FROM colors WHERE name = 'red'),'BMW'),
-- ((SELECT color_id FROM colors WHERE name = 'grey'),'Ferrari');

-- SELECT * FROM cars_restrict

--trying to delete one of the colors from the table colors (parent)


-- ON DELETE CASCADE OPTION 

-- DELETE FROM colors WHERE color_id=1
--  update or delete on table "colors" violates foreign key constraint "cars_restrict_car_color_fkey" on table "cars_restrict"
-- Key (color_id)=(1) is still referenced from table "cars_restrict". 

-- CREATE TABLE cars_cascade(
-- car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON UPDATE CASCADE ON DELETE CASCADE,
-- car_name TEXT);

-- INSERT INTO cars_cascade (car_color, car_name)
-- VALUES
-- ((SELECT color_id FROM colors WHERE name = 'black'),'Mazda'),
-- ((SELECT color_id FROM colors WHERE name = 'red'),'BMW'),
-- ((SELECT color_id FROM colors WHERE name = 'grey'),'Ferrari');

-- DELETE FROM colors WHERE color_id = 1;

-- UPDATE colors SET color_id = 4 WHERE name = 'red';



-- CREATE TABLE cars_null 
-- (car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE SET NULL,
-- car_name TEXT);

-- INSERT INTO cars_null (car_color, car_name)
-- VALUES
-- ((SELECT color_id FROM colors WHERE name = 'red'),'BMW'),
-- ((SELECT color_id FROM colors WHERE name = 'grey'),'Ferrari');

-- DELETE FROM colors WHERE color_id = 3;

-- SELECT * FROM cars_null