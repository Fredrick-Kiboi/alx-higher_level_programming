-- script that creates the table unique_id
-- unique_id description: id INT default 1 and must be unique, name VARCHAR(256)
-- if table exists, script shouldn't fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

