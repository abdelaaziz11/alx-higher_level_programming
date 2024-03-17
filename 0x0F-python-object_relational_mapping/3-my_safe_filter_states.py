#!/usr/bin/python3

"""
The same thing like the file 2-my_filter_states.py .
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )

    cursor = connection.cursor()

    sql_query = " SELECT * FROM states WHERE BINARY name = %s "
    cursor.execute(sql_query, (argv[4],))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
