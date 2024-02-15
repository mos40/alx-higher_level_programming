-- 10-top_score.sql
-- Lists all records of the table second_table in the specified database ordered by score (top first)
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
