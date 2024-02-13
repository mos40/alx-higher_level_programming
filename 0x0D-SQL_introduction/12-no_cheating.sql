-- 12-no_cheating.sql
-- Updates the score of Bob to 10 in the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
