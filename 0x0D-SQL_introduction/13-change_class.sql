-- 13-change_class.sql
-- Removes all records with a score <= 5 in the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

DELETE FROM second_table
WHERE score <= 5;
