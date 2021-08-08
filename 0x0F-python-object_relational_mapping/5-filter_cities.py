#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON \
                    cities.state_id=states.id \
                    WHERE states.name=%s", (sys.argv[4],))
    for i in cursor.fetch_row():
        print(i)
    cursor.close()
    db.cursor()
