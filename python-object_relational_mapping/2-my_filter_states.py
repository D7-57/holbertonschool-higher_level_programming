#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and the searched state name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor and execute the query
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print matching results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
