-- Task: 4. ID can't be null

-- Check if the table id_not_null already exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
