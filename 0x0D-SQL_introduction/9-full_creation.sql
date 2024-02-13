-- 9-full_creation.sql
-- Creates a table second_table in the specified database and adds multiple rows

USE `hbtn_0c_0`;  -- Replace 'hbtn_0c_0' with the actual database name

-- Create the second_table if it does not exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Add multiple rows to second_table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
