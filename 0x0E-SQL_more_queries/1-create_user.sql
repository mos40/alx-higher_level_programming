-- Task: 0. My privileges!
-- Show grants for user_0d_1
-- Show grants for user_0d_2
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
