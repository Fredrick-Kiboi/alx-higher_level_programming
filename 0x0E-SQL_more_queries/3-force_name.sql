-- script that creates the table force_name on my MySQL server
-- force name description: id INT, name VARCHAR(256) can't be null
-- the database name will be passed an argument
-- if the table exists, script shouldn't fail
USE hbtn_0d_2;
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

