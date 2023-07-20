-- script that create the table id_not_null
-- id_not_null description: id INT with default value 1, name VARCHAR(256)
-- if table doesn't exist, script should not fail
-- database name will be passed as an argument
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));

