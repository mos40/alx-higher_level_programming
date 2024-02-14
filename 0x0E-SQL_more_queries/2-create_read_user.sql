-- Task: 2. Read user

-- Check if the database hbtn_0d_2 already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Check if the user user_0d_2 already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges to user_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
