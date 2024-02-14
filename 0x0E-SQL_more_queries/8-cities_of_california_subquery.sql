-- Task: 8. Cities of California

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Select cities of California using a subquery
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
