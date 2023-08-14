-- script to add a bunch of cities in the cities table
use hbtn_0d_usa;
INSERT INTO cities(id, state_id, name)
VALUES
(2, 1, "San Jose"),
(4, 2, "Page"),
(6, 3, "Paris"),
(7, 3, "Houston"),
(8, 3, "Dallas");
