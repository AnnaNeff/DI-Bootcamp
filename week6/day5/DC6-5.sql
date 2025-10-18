SET search_path TO movies

-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. Use window functions to determine the budget growth rate and then calculate the average growth rate.

WITH company_movie_budgets AS (
  SELECT pc.company_name, m.movie_id, m.title, m.release_date, m.budget,
  LAG(m.budget) OVER ( PARTITION BY pc.company_name ORDER BY m.release_date, m.movie_id ) AS prev_budget
  FROM movie m
  JOIN movie_company mc ON mc.movie_id = m.movie_id
  JOIN production_company pc ON pc.company_id = mc.company_id
),
growth AS (
  SELECT company_name, title, release_date, budget,
    CASE
      WHEN prev_budget IS NULL THEN NULL
      ELSE (budget - prev_budget) / NULLIF(prev_budget, 0.0)
    END AS budget_growth_rate
  FROM company_movie_budgets
)
SELECT
  company_name,
  AVG(budget_growth_rate) AS avg_budget_growth_rate
FROM growth
WHERE budget_growth_rate IS NOT NULL
GROUP BY company_name
ORDER BY avg_budget_growth_rate DESC NULLS LAST, company_name

-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.

WITH movie_with_global_avg AS (
  SELECT
    m.movie_id,
    m.vote_average,
    AVG(m.vote_average) OVER () AS global_avg_rating
  FROM movie m
),
actor_above_avg AS (
  SELECT
    p.person_id,
    p.person_name,
    COUNT(DISTINCT mc.movie_id) FILTER (
      WHERE mwa.vote_average > mwa.global_avg_rating
    ) AS above_avg_count
  FROM movie_cast mc
  JOIN person p ON p.person_id = mc.person_id
  JOIN movie_with_global_avg mwa ON mwa.movie_id = mc.movie_id
  GROUP BY p.person_id, p.person_name
),
ranked AS (
  SELECT
    person_name,
    above_avg_count,
    RANK() OVER (ORDER BY above_avg_count DESC) AS rnk
  FROM actor_above_avg
)
SELECT person_name, above_avg_count
FROM ranked
WHERE rnk = 1
ORDER BY person_name

-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. Use window functions with the ROWS frame specification to achieve this.

SELECT
  g.genre_name,
  m.title,
  m.release_date,
  m.revenue,
  AVG(m.revenue) OVER (
    PARTITION BY g.genre_name
    ORDER BY m.release_date, m.movie_id
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS rolling_avg_revenue_last3
FROM movie m
JOIN movie_genres mg ON mg.movie_id = m.movie_id
JOIN genre g ON g.genre_id = mg.genre_id
ORDER BY g.genre_name, m.release_date, m.movie_id

-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions and CTEs to group movies by their series and calculate the total revenue.

WITH kw_rev AS (
  SELECT
    k.keyword_id,
    k.keyword_name,
    m.movie_id,
    m.title,
    m.revenue,
    SUM(m.revenue) OVER (PARTITION BY k.keyword_id) AS total_revenue_by_series
  FROM movie m
  JOIN movie_keywords mk ON mk.movie_id = m.movie_id
  JOIN keyword k ON k.keyword_id = mk.keyword_id
),
series_rank AS (
  SELECT DISTINCT
    keyword_id,
    keyword_name,
    total_revenue_by_series,
    RANK() OVER (ORDER BY total_revenue_by_series DESC) AS rnk
  FROM kw_rev
)
SELECT
  sr.keyword_name AS series_name,
  sr.total_revenue_by_series
FROM series_rank AS sr
WHERE sr.rnk = 1
ORDER BY sr.keyword_name