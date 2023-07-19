-- script that converts hbtn_0c_0 database to UTF8
-- You need to convert all of the following:
-- Database hbtn_0c_0, Table first_table, Field name in first_table
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY id INT;
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;

