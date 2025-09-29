SELECT * FROM actors
SELECT COUNT(*) FROM actors
INSERT INTO actors (first_name,last_name,date_of_birth,oscars)
VALUES
('Emma', 'Watson', '04/15/1990', NULL)

-- Outcome: "ERROR:  null value in column "oscars" of relation "actors" violates not-null constraint"
	-- "Failing row contains (11, Emma, Watson, 1990-04-15, null)."

