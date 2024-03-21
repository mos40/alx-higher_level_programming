#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to select states starting with 'N'
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        # Print the fetched result
        for row in results:
            print(row)
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # Disconnect from server
    db.close()
