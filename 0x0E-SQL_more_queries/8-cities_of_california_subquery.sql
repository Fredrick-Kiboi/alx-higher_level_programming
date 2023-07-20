-- script that lists all the cities of California in database hbtn_0d_usa
-- The states table contains only one record where name = california (but id can be different)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use JOIN
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities WHERE cities.name = 'california' ORDER BY cities.id ASC
UNION
SELECT states.id, states.name FROM states WHERE states.name = 'california';

