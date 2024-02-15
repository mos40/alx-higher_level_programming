-- 12-no_cheating.sql
-- Updates the score of Bob to 10 in the table second_table in the specified database
UPDATE `second_table`
SET `score` = 10
WHERE `name` = "Bob";
