-- 14-average.sql
-- Computes the score average of all records in the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

SELECT AVG(score) AS average
FROM second_table;
