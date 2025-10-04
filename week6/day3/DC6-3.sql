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

-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film 
SET language_id = 2
WHERE 
title = 'Chamber Italian'

SELECT * FROM film
WHERE  title = 'Chamber Italian'

-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

--The customer table has two foreign keys:
-- store_id and address_id.

-- We must use an existing store_id and an existing address_id (not null).
-- So usually we create/select the address first, then insert the customer with those ids.
-- If the ids don’t exist, the insert fails with a foreign-key error.

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

DROP TABLE customer_review
-- Query returned successfully

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT MAX(return_date ) FROM rental
--As there is no date more then today (04.10.2025) in the return_date colum, let's set that today is 2 February 2005
SELECT COUNT(*)
FROM rental
WHERE return_date > '2005-8-02'

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
SELECT * FROM rental AS r
INNER JOIN payment AS p
ON r.rental_id = p.rental_id
WHERE return_date > '2005-8-02'
ORDER BY p.amount DESC
LIMIT 30

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT * FROM film AS f
FULL JOIN film_actor as fa
ON f.film_id = fa.film_id
LEFT JOIN actor AS a
ON a.actor_id = fa.actor_id
WHERE f.description LIKE '%Sumo%Wrestler%' AND a.first_name = 'Penelope' and a.last_name = 'Monroe'

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT * FROM film AS f
INNER JOIN film_category as fc
ON f.film_id = fc.film_id
LEFT JOIN category AS c
ON c.category_id = fc.category_id
WHERE f.length < 60 AND f.rating = 'R' AND c.name = 'Documentary'

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT * FROM film AS f
INNER JOIN inventory as i
ON f.film_id = i.film_id
INNER JOIN rental AS r
ON i.inventory_id = r.inventory_id
INNER JOIN payment AS p
ON r.rental_id = p.rental_id
INNER JOIN customer as c
ON r.customer_id = c.customer_id

WHERE c.first_name = 'Matthew' 
AND c.last_name = 'Mahan' 
AND p.amount > 4 
AND r.return_date BETWEEN '2005-7-28' AND '2005-08-01'

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT * FROM film AS f
INNER JOIN inventory as i
ON f.film_id = i.film_id
INNER JOIN rental AS r
ON i.inventory_id = r.inventory_id
INNER JOIN payment AS p
ON r.rental_id = p.rental_id
INNER JOIN customer as c
ON r.customer_id = c.customer_id

WHERE c.first_name = 'Matthew' 
AND c.last_name = 'Mahan' 
AND (f.title LIKE '%Boat%' OR f.description LIKE '%Boat%')

ORDER BY f.replacement_cost DESC
LIMIT 1