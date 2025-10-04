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