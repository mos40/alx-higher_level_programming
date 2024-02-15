-- 16-no_link.sql
-- Lists all records of the table second_table in the specified database

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
