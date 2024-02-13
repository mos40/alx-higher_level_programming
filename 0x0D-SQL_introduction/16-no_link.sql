-- 16-no_link.sql
-- Lists all records of the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
