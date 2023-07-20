-- script that creates the database hbtn_0d_usa and the table cities in the database
-- cities description:
-- id INT unique, auto generated, can't be null and is primary key
-- state_id INT, can't be null, must be a FOREIGN KEY, that references to id
-- if database exists, you script should not fail
-- if tables exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id));
ALTER TABLE cities AUTO_INCREMENT = 1;

