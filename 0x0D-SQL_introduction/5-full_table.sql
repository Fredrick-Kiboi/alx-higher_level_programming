-- script that prints the full description of the table first_table
-- the database name will be passed as an argument
-- you are not allowed to use DESCRIBE or EXPLAIN
USE INFORMATION_SCHEMA;
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_TYPE FROM COLUMNS WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
