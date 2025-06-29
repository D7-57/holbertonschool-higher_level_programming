#!/usr/bin/python3
"""Safely displays states where name matches the argument"""

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

    # Create a cursor and safely execute a parameterized query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = \
     %s ORDER BY id ASC", (state_name,))

    # Fetch and print matching results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
