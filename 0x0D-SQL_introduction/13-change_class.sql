-- 13-change_class.sql
-- Removes all records with a score <= 5 in the table second_table in the specified database
DELETE FROM `second_table`
WHERE `score` <= 5;
