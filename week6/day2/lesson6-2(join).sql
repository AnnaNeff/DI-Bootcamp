--JOINS IN SQL

--INNER JOIN

SELECT actors.first_name, actors.last_name, movies.movie_title
FROM actors
INNER JOIN movies
ON actors.actor_id = movies.actor_playing_id

CREATE TABLE producers(
producer_id SERIAL,
producer_name VARCHAR (50) NOT NULL,
movie_created_id INTEGER,
PRIMARY KEY (producer_id),
FOREIGN KEY (movie_created_id) REFERENCES movies (movie_id)
)

INSERT INTO producers (producer_name, movie_created_id) VALUES
    ( 'J. J. Abrams', 
    (SELECT movie_id from movies WHERE movie_title='Good Will Hunting')),
	('Jarry Weintraub', (SELECT movie_id from movies WHERE movie_title='Oceans Eleven'))

INSERT INTO producers (producer_name, movie_created_id) VALUES
	('Christofer Nolan', NULL)

SELECT * FROM producers

SELECT *
FROM movies AS m
INNER JOIN producers AS p
ON p.movie_created_id = m.movie_id

--LEFT JOIN

SELECT p.producer_name, m.movie_title
FROM producers AS p
LEFT JOIN movies AS m
ON p.movie_created_id = m.movie_id

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Harry Potter', 'Srory',
    (SELECT actor_id from actors WHERE first_name='Emma' AND last_name='Watson'))
	
SELECT * FROM movies

--FULL JOIN
SELECT p.producer_name, m.movie_title
FROM producers AS p
FULL JOIN movies AS m
ON p.movie_created_id = m.movie_id
