-- script that create the MySQL server user user_0d_1
-- the user should have all privileges on your server
-- the user password should be set to user_0d_1_pwd
-- If user already exist, you script should not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
