-- Task 1: Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
SET search_path TO olympics, public;

CREATE TEMP TABLE tmp_bi_season_medalists AS
SELECT
  p.id AS person_id, p.full_name,
  (
    SELECT COUNT(*)
    FROM games_competitor gc2
    JOIN competitor_event ce2 ON ce2.competitor_id = gc2.id
    JOIN medal m2 ON m2.id = ce2.medal_id
    JOIN games g2 ON g2.id = gc2.games_id
    WHERE gc2.person_id = p.id
      AND g2.season = 'Summer'
      AND m2.medal_name <> 'NA'
  ) AS summer_medals,
  (
    SELECT COUNT(*)
    FROM games_competitor gc3
    JOIN competitor_event ce3 ON ce3.competitor_id = gc3.id
    JOIN medal m3 ON m3.id = ce3.medal_id
    JOIN games g3 ON g3.id = gc3.games_id
    WHERE gc3.person_id = p.id
      AND g3.season = 'Winter'
      AND m3.medal_name <> 'NA'
  ) AS winter_medals
FROM person p
WHERE EXISTS (
  SELECT 1
  FROM games_competitor gc
  JOIN competitor_event ce ON ce.competitor_id = gc.id
  JOIN medal m ON m.id = ce.medal_id
  JOIN games g ON g.id = gc.games_id
  WHERE gc.person_id = p.id AND g.season = 'Summer' AND m.medal_name <> 'NA'
)
AND EXISTS (
  SELECT 1
  FROM games_competitor gc
  JOIN competitor_event ce ON ce.competitor_id = gc.id
  JOIN medal m ON m.id = ce.medal_id
  JOIN games g ON g.id = gc.games_id
  WHERE gc.person_id = p.id AND g.season = 'Winter' AND m.medal_name <> 'NA'
);

SELECT * FROM tmp_bi_season_medalists
ORDER BY (summer_medals + winter_medals) DESC, full_name

-- Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMP TABLE tmp_two_sport_medalists AS
SELECT
  p.id AS person_id, p.full_name,
  (
    SELECT COUNT(*)
    FROM games_competitor gc2
    JOIN competitor_event ce2 ON ce2.competitor_id = gc2.id
    JOIN medal m2 ON m2.id = ce2.medal_id
    WHERE gc2.person_id = p.id
      AND m2.medal_name <> 'NA'
  ) AS total_medals
FROM person p
WHERE p.id IN (
  SELECT gc.person_id
  FROM games_competitor gc
  JOIN competitor_event ce ON ce.competitor_id = gc.id
  JOIN event e ON e.id = ce.event_id
  JOIN sport s ON s.id = e.sport_id
  JOIN medal m ON m.id = ce.medal_id
  WHERE m.medal_name <> 'NA'
  GROUP BY gc.person_id
  HAVING COUNT(DISTINCT s.id) = 2
);

SELECT person_id, full_name, total_medals
FROM tmp_two_sport_medalists
ORDER BY total_medals DESC, full_name
LIMIT 3


-- 🌟 Exercise 2: Region and Competitor Performance
-- Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
WITH max_event_medals_per_person AS (
  SELECT
    t.person_id,
    MAX(cnt_medals_in_event) AS max_medals_in_single_event
  FROM (
    SELECT
      gc.person_id,
      ce.event_id,
      COUNT(*) AS cnt_medals_in_event
    FROM games_competitor AS gc
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    JOIN medal m ON m.id = ce.medal_id
    WHERE m.medal_name <> 'NA'
    GROUP BY gc.person_id, ce.event_id
  ) t
  GROUP BY t.person_id
)
SELECT
  nr.region_name,
  SUM(mep.max_medals_in_single_event) AS total_max_medals
FROM max_event_medals_per_person mep
JOIN person_region pr ON pr.person_id = mep.person_id
JOIN noc_region nr    ON nr.id = pr.region_id
GROUP BY nr.region_name
ORDER BY total_max_medals DESC, nr.region_name
LIMIT 5

-- Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.

CREATE TEMP TABLE tmp_many_games_no_medals AS
SELECT
  p.id AS person_id,
  p.full_name,
  (
    SELECT COUNT(DISTINCT gc2.games_id)
    FROM games_competitor gc2
    WHERE gc2.person_id = p.id
  ) AS games_count
FROM person p
WHERE (
  SELECT COUNT(DISTINCT gc3.games_id)
  FROM games_competitor gc3
  WHERE gc3.person_id = p.id
) > 3
AND NOT EXISTS (
  SELECT 1
  FROM games_competitor gc4
  JOIN competitor_event ce4 ON ce4.competitor_id = gc4.id
  JOIN medal m4 ON m4.id = ce4.medal_id
  WHERE gc4.person_id = p.id
    AND m4.medal_name <> 'NA'
);

SELECT person_id, full_name, games_count
FROM tmp_many_games_no_medals
ORDER BY games_count DESC, full_name