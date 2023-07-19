-- script that converts hbtn_0c_0 database to UTF8
-- You need to convert all of the following:
-- Database hbtn_0c_0, Table first_table, Field name in first_table
-- Step 1: Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 2: Convert the table
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Step 3: Convert the field
ALTER TABLE hbtn_0c_0.first_table MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

