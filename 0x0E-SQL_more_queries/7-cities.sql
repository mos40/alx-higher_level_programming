-- Task: 7. Cities table

-- Check if the database hbtn_0d_usa already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Check if the table cities already exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert sample data
INSERT INTO cities (state_id, name) VALUES (1, 'San Francisco');
