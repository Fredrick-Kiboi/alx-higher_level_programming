-- script that lists all cities in database hbtn_0d_usa
  -- Each record should display: cities.id - cities.name - states.name
  -- Results should be in ascending order by cities.id
  -- You can use only one SELECT statement
use hbtn_0d_usa;
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;

