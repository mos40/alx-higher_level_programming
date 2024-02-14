-- Task: 5. Unique ID

-- Check if the table unique_id already exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
