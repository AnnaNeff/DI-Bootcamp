CREATE TABLE IF NOT EXISTS sample_data (id INT, value INT);
INSERT INTO sample_data (id, value) VALUES (1, 10), (2, NULL), (3, 30)

SELECT id, value FROM sample_data WHERE value is NULL
SELECT id, COALESCE(value, id*10) AS imputed_value FROM sample_data

DROP TABLE IF EXISTS sample_data

CREATE TABLE sample_data (id INT, value INT);
INSERT INTO sample_data (id, value) VALUES (1, 10), (2, 20), (3, 10)

SELECT id, value, 
	ROW_NUMBER() OVER (PARTITION BY value) as row_number
FROM sample_data

-- Sample data
CREATE TABLE sample_data (id INT, value VARCHAR(50));
INSERT INTO sample_data (id, value) VALUES (1, 'apple'), (2, 'Apple'), (3, 'APPLE')

SELECT id, UPPER(value) FROM sample_data
UPDATE sample_data

CREATE TABLE exercise_data (
    id INT,
    date VARCHAR(50),
    value INT,
    status VARCHAR(1)
);

INSERT INTO exercise_data (id, date, value, status) VALUES
(1, '2021-01-01', 10, 'A'),
(2, '2021-01-02', NULL, 'I'),
(3, '2021-01-03', -5, 'A'),
(4, '2021-01-04', 20, 'X')