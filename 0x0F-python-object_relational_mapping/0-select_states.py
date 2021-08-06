#!/usr/bin/python
""" lists all states from the database """
import MySQLdb
import sys

if __name__ == '__main__':
db = _mysql.connect(
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    host="localhost",
    port=3306)
cursor = db.cursor()
sql = """SELECT * FROM states ORDER BY states.id ASC"""
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)
cursor.close()
db.close()
