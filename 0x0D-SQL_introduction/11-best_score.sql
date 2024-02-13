-- 11-best_score.sql
-- Lists all records with a score >= 10 in the table second_table in the specified database

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
