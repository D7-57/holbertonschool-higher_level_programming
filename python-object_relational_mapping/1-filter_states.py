#!/usr/bin/python3
"""Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def main():
    """Main logic: connect to DB, execute query, print filtered states"""
    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()

# Ensure code is not executed when imported
if __name__ == "__main__":
    main()
