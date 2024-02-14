# MySQL Privileges Script

## Description

This project contains a script (`0-privileges.sql`) to list the privileges of MySQL users `user_0d_1` and `user_0d_2` on the local server.

## Prerequisites

- MySQL 8.0.25
- Ubuntu 20.04 LTS

## Setup

1. Ensure MySQL is installed on your system.
2. Create the MySQL users:

    ```bash
    echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
    echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
    ```

3. Grant privileges to `user_0d_1`:

    ```bash
    echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
    ```

## Usage

Run the script to list privileges:

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
