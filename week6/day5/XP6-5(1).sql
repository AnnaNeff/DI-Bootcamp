SET search_path TO movies
-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.

SELECT g.genre_name, m.title,
	RANK () OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS pop_rank_by_genre
FROM movie AS m
LEFT JOIN movie_genres AS mg
ON m.movie_id = mg.movie_id
FULL JOIN genre AS g
ON g.genre_id = mg.genre_id

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.

SELECT * FROM 
(SELECT pc.company_name, m.title, m.revenue, 
NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC ) AS revenue_quartile, 
ROW_NUMBER() OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS rn
FROM movie AS m
INNER JOIN movie_company AS mc ON m.movie_id = mc.movie_id
INNER JOIN production_company AS pc ON mc.company_id = pc.company_id)
WHERE rn <= 3


-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.

SELECT g.genre_name, m.title, m.budget, 
	SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.release_date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_budget
FROM movie AS m
JOIN movie_genres AS mg ON mg.movie_id = m.movie_id
JOIN genre AS g ON g.genre_id = mg.genre_id

-- Task 4: Identify the Most Recent Movie for Each Genre

-- Use the FIRST_VALUE() function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.

SELECT genre_name, most_recent_title, most_recent_date FROM 
(SELECT genre_name, 
	FIRST_VALUE(m.title) OVER (PARTITION BY genre_name ORDER BY m.release_date DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS most_recent_title,
  	FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS most_recent_date,
	ROW_NUMBER() OVER (PARTITION BY genre_name ORDER BY m.release_date DESC) AS rn
FROM movie AS m
JOIN movie_genres AS mg ON mg.movie_id = m.movie_id
JOIN genre AS g ON g.genre_id = mg.genre_id)
WHERE rn = 1

-- Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies

-- Use the DENSE_RANK() function to rank actors based on the number of movies they have appeared in. Display the actor’s name and their rank.

SELECT p.person_name,
DENSE_RANK() OVER (ORDER BY number_of_movies DESC) AS actor_rank
FROM person AS p
JOIN (
	SELECT person_id, COUNT(DISTINCT movie_id) AS number_of_movies
	FROM movie_cast GROUP BY person_id
	) AS nm ON p.person_id = nm.person_id
	
-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average movie rating. Display the director’s name and their average rating.

WITH director_rank AS (
	SELECT p.person_name, AVG(m.vote_average) AS vote_average 
	FROM movie_crew AS mc
	JOIN person AS p ON mc.person_id = p.person_id
	JOIN movie AS m ON mc.movie_id = m.movie_id
	WHERE mc.job = 'Director'
	GROUP BY p.person_name
	ORDER BY vote_average DESC
	)

SELECT person_name,
RANK() OVER(ORDER BY vote_average DESC)
FROM director_rank

-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted by each actor. Display the actor’s name and the cumulative revenue.

SELECT p.person_name, SUM(m.revenue) AS cum_rev 
FROM movie_cast AS mc
JOIN person AS p ON mc.person_id = p.person_id
JOIN movie AS m ON mc.movie_id = m.movie_id
GROUP BY p.person_name
ORDER BY cum_rev DESC

-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget

-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director’s name and the total budget.
WITH total_budget AS (
	SELECT * FROM movie_crew AS mc
	JOIN person AS p ON mc.person_id = p.person_id
	JOIN movie AS m ON mc.movie_id = m.movie_id
	WHERE mc.job = 'Director'
	)
SELECT person_name, SUM (budget) AS movies_budget FROM total_budget
GROUP BY person_name
ORDER BY movies_budget DESC