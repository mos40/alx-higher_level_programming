-- 8-count_89.sql
-- Displays the number of records with id = 89 in the table first_table of the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

SELECT COUNT(*) FROM first_table WHERE id = 89;
