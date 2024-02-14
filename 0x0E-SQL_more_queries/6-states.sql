-- Task: 6. States table

-- Check if the database hbtn_0d_usa already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Check if the table states already exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert sample data
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
