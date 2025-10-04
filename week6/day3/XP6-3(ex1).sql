-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.

SELECT name FROM language

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.

SELECT f.title, f.description, l.name AS language
FROM film AS f
LEFT JOIN language AS l
ON f.language_id = l.language_id

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

SELECT f.title, f.description, l.name AS language
FROM film AS f
RIGHT JOIN language AS l
ON f.language_id = l.language_id

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

CREATE TABLE new_film (
id SERIAL,
name VARCHAR(45) NOT NULL,
PRIMARY KEY (id)
)

INSERT INTO new_film (name) VALUES
('Harry Potter and the Philosopher Stone'), 
('Harry Potter and the Chamber of Secrets'), 
('Harry Potter and the Prisoner of Azkaban'),
('Harry Potter and the Goblet of Fire'),
('Harry Potter and the Order of the Phoenix'),
('Harry Potter and the Half-Blood Prince'),
('Harry Potter and the Deathly Hallows – Part 1'),
('Harry Potter and the Deathly Hallows – Part 2')

-- Create a new table called customer_review, which will contain film reviews that customers will make.

-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

CREATE TABLE customer_review(
review_id SERIAL NOT NULL PRIMARY KEY,
film_id INTEGER,
language_id INTEGER,
title VARCHAR (100),
score INTEGER CHECK (score >= 1 AND score <= 10),
review_text TEXT,
last_update DATE,
FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
FOREIGN KEY (language_id) REFERENCES language(language_id) ON DELETE SET NULL
)

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review(film_id, language_id, title, score, review_text, last_update) 
VALUES
((SELECT id FROM new_film WHERE name = 'Harry Potter and the Philosopher Stone'),
(SELECT language_id FROM language WHERE name = 'English'),
'Good family movie', 10, 'Grate movie to see with family and friends! I love it', '2025-10-04'),

((SELECT id FROM new_film WHERE name = 'Harry Potter and the Chamber of Secrets'),
(SELECT language_id FROM language WHERE name = 'French'),
'Bon film familial', 9, 'Super film à voir en famille et entre amis ! Jadore', '2024-09-05'),

((SELECT id FROM new_film WHERE name = 'Harry Potter and the Prisoner of Azkaban'),
(SELECT language_id FROM language WHERE name = 'German'),
'Guter Familienfilm', 8, 'Toller Film für die ganze Familie und Freunde! Ich liebe ihn', '2023-08-07')

SELECT * FROM customer_review

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?

DELETE FROM new_film where name = 'Harry Potter and the Chamber of Secrets'

SELECT * FROM customer_review
-- The row with review was also deleted
