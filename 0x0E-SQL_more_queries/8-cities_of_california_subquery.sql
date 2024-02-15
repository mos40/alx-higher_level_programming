-- Task: 8. Cities of California
-- Select cities of California using a subquery
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
