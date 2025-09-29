-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  date_of_birth DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )

-- SELECT * FROM actors

-- ADD DATA INTO THE TABLE

-- INSERT INTO actors (first_name,last_name,date_of_birth,number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)

-- INSERT INTO actors (first_name,last_name,date_of_birth,number_oscars)
-- VALUES ('Jannifer', 'Aniston', '11/02/1969', 1)

-- INSERT INTO actors (first_name,last_name,date_of_birth,number_oscars)
-- VALUES ('Audrey', 'Hepburn', '04/05/1929', 1)

-- INSERT INTO actors (first_name,last_name,date_of_birth,number_oscars)
-- VALUES
-- ('Charlie', 'Hunnam', '10/04/1980', 0),
-- ('Katharine', 'Hepburn', '12/05/1907', 4),
-- ('Leonardo', 'DiCaprio', '11/11/1974', 1)

-- SELECT * FROM actors;

--different ways TO RETRIVE AND DISPLAY THE DATA USING SELECT

-- SELECT first_name, last_name FROM actors

-- ADDING CONDITIONS USING WHERE

-- SELECT * FROM actors WHERE number_oscars > 1
-- SELECT * FROM actors WHERE first_name = 'Jannifer' AND last_name = 'Aniston'


-- INSERT INTO actors (first_name, last_name, date_of_birth, number_oscars)
-- VALUES ('Matt', 'Perry', '08/19/1969', 0)

-- UPDATE, DELETE, ALTER
-- SELECT * FROM actors
-- UPDATE actors
-- SET date_of_birth = '11/11/1975' WHERE first_name = 'Leonardo'
-- RETURNING 
-- *

--UPDATINT THE TABLE

-- ALTER TABLE actors RENAME COLUMN number_oscars TO oscars;
-- SELECT * FROM actors 

--DELETING A ROW
-- DELETE FROM actors WHERE actor_id = 7
SELECT * FROM actors





