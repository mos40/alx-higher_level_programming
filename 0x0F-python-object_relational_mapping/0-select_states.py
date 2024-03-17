#!/usr/bin/python3
import MySQLdb
import sys


def main():
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL credentials from command line arguments
    username, password, database = sys.argv[1:]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=username,
                             passwd=password, db=database)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select all states and order by id
    try:
        cursor.execute("SELECT * FROM states ORDER BY id")
    except MySQLdb.Error as e:
        print("Error executing SQL query:", e)
        db.close()
        sys.exit(1)

    # Fetch all rows from the result
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
