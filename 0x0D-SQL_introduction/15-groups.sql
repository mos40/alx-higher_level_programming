-- 15-groups.sql
-- Lists the number of records with the same score in the table second_table in the specified database

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
