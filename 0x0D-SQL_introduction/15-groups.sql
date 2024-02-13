-- 15-groups.sql
-- Lists the number of records with the same score in the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC, score DESC;
