-- Task: 9. Cities by States
-- Use the hbtn_0d_usa database
-- Select cities and states using a JOIN
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
