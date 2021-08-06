#!/usr/bin/python3
""" Script takes an argument and displays values """
import MYSQLdb
import sys

if __name__ == '__main__':

    db = MYSQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY {:s} \
                    ORDER BY states.id ASC".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
