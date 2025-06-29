#!/usr/bin/python3
"""Lists all cities of a given state from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials and state name from arguments
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

    # Create cursor and safely execute a JOIN query with parameter
    cur = db.cursor()
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch results and format output
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    # Clean up
    cur.close()
    db.close()
