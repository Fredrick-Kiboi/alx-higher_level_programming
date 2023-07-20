-- script that creates the database hbtn_0d_usa and the table cities in the database
-- cities description:
-- id INT unique, auto generated, can't be null and is primary key
-- state_id INT, can't be null, must be a FOREIGN KEY, that references to id
-- if database exists, you script should not fail
-- if tables exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLES IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT FOREIGN KEY NOT NULL REFERENCES cities (id), name VARCHAR(256) NOT NULL);
ALTER TABLE cities AUTO_INCREMENT = 1;

