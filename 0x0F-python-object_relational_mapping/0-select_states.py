#!/usr/bin/python3
from sys import argv
import MySQLdb

if __name__ == "__main__":

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
