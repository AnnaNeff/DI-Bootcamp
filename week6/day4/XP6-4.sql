SET search_path TO olympics, public
-- Task 1: Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.

-- SELECT m.medal_name, AVG(gc.age)
-- FROM games_competitor AS gc
-- JOIN competitor_event AS ce
--   ON ce.competitor_id = gc.id
-- JOIN medal AS m
--   ON m.id = ce.medal_id
-- WHERE (
--   SELECT COUNT(*)
--   FROM competitor_event AS ce2
--   WHERE ce2.competitor_id = gc.id
--     AND ce2.medal_id IS NOT NULL
-- ) > 0
-- GROUP BY m.medal_name

SELECT m.medal_name, AVG(gc.age)
FROM games_competitor AS gc
JOIN competitor_event AS ce
  ON ce.competitor_id = gc.id
JOIN medal AS m
  ON m.id = ce.medal_id
WHERE m.medal_name != 'NA'
GROUP BY m.medal_name

-- Task 2: Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.

SELECT nr.region_name,
       COUNT(DISTINCT pr_filtered.person_id) AS unique_competitors
FROM (
    SELECT pr.person_id, pr.region_id
    FROM person_region AS pr
    WHERE pr.person_id IN (
        SELECT gc.person_id
        FROM games_competitor AS gc
        JOIN competitor_event ce ON ce.competitor_id = gc.id
        GROUP BY gc.person_id
        HAVING COUNT(DISTINCT ce.event_id) > 3
    )
) AS pr_filtered
JOIN noc_region nr ON nr.id = pr_filtered.region_id
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5

-- Task 3: Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.

DROP TABLE IF EXISTS tmp_medals_by_competitor;

CREATE TEMP TABLE tmp_medals_by_competitor AS
SELECT gc.id AS competitor_id,
       (
         SELECT COUNT(*)
         FROM competitor_event ce2
         JOIN medal m2 ON m2.id = ce2.medal_id
         WHERE ce2.competitor_id = gc.id
           AND m2.medal_name <> 'NA'
       ) AS medals_total
FROM games_competitor gc

-- Task 4: Use a subquery within a DELETE statement to remove records of competitors who have not won any medals from a temporary table created for analysis.

DELETE FROM tmp_medals_by_competitor t
WHERE NOT EXISTS (
  SELECT 1
  FROM competitor_event ce
  WHERE ce.competitor_id = t.competitor_id
    AND ce.medal_id IS NOT NULL
)

-- Task 1: Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

UPDATE person p
SET height = (
  SELECT AVG(p2.height)
  FROM person p2
  JOIN person_region pr2 ON pr2.person_id = p2.id
  WHERE pr2.region_id IN (
    SELECT pr.region_id
    FROM person_region pr
    WHERE pr.person_id = p.id
  )
)
WHERE EXISTS (
  SELECT 1 FROM person_region pr WHERE pr.person_id = p.id
)

-- Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.

CREATE TEMP TABLE tmp_multi_event_competitors (
  competitor_id INT,
  person_id     INT,
  games_id      INT,
  total_events  INT
);

INSERT INTO tmp_multi_event_competitors (competitor_id, person_id, games_id, total_events)
SELECT
  gc.id            AS competitor_id,
  gc.person_id,
  gc.games_id,
  (
     SELECT COUNT(DISTINCT ce2.event_id)
     FROM competitor_event ce2
     WHERE ce2.competitor_id = gc.id
  ) AS total_events
FROM games_competitor gc
WHERE gc.id IN (
  SELECT ce.competitor_id
  FROM competitor_event ce
  GROUP BY ce.competitor_id
  HAVING COUNT(DISTINCT ce.event_id) > 1
);

SELECT * FROM tmp_multi_event_competitors
ORDER BY total_events DESC, competitor_id

-- Task 3: Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.

SELECT nr.region_name,
       AVG(pp.medals_per_person) AS avg_medals_per_competitor
FROM (
    SELECT p.id AS person_id,
           COUNT(*) AS medals_per_person
    FROM person p
    JOIN games_competitor gc ON gc.person_id = p.id
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    JOIN medal m ON m.id = ce.medal_id
    WHERE m.medal_name <> 'NA'
    GROUP BY p.id
) AS pp
JOIN person_region pr ON pr.person_id = pp.person_id
JOIN noc_region nr     ON nr.id = pr.region_id
GROUP BY nr.region_name
HAVING AVG(pp.medals_per_person) > (
    SELECT AVG(sub.medals_per_person)
    FROM (
        SELECT p2.id AS person_id,
               COUNT(*) AS medals_per_person
        FROM person p2
        JOIN games_competitor gc2 ON gc2.person_id = p2.id
        JOIN competitor_event ce2 ON ce2.competitor_id = gc2.id
        JOIN medal m2 ON m2.id = ce2.medal_id
        WHERE m2.medal_name <> 'NA'
        GROUP BY p2.id
    ) AS sub
)
ORDER BY avg_medals_per_competitor DESC

-- Task 4: Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.

CREATE TEMP TABLE tmp_person_seasons AS
SELECT
  p.id AS person_id,
  EXISTS (
    SELECT 1
    FROM games_competitor gc
    JOIN games g ON g.id = gc.games_id
    WHERE gc.person_id = p.id
      AND g.season = 'Summer'
  ) AS has_summer,
  EXISTS (
    SELECT 1
    FROM games_competitor gc
    JOIN games g ON g.id = gc.games_id
    WHERE gc.person_id = p.id
      AND g.season = 'Winter'
  ) AS has_winter
FROM person p;

SELECT t.person_id, p.full_name
FROM tmp_person_seasons t
JOIN person p ON p.id = t.person_id
WHERE t.has_summer AND t.has_winter
ORDER BY p.full_name