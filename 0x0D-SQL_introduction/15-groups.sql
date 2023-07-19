-- script that lists the number of records with the same score in the second_table
-- result should display: the score, the number of records with the same score
-- the list should be in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;

