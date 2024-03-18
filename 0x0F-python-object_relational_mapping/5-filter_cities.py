#!/usr/bin/python3
"""script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
            )

    cursor = connection.cursor()

    cursor.execute("SELECT cities.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = '{}'".format(argv[4]))

    results = cursor.fetchall()

    """cities = [row[0] for row in results]
    print(", ".join(cities))"""

    cities = list(map(lambda row: row[0], results))
    print(", ".join(cities))

