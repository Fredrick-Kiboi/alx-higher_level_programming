-- script that creates a table called first_table
-- database name will be passed as an argument of the mysql command
-- if the table first_table already exists, script shouldn't fail
CREATE TABLE IF NOT EXISTS first_table (id INT,	name VARCHAR(256));

