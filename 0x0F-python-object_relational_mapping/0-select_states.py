#!/usr/bin/python
# script that lists all states from the database hbtn_0e_0_usa
from MySQLdb import _mysql


db = _mysql.connect(user="alx",passwd="1234",db="hbtn_0e_0_usa")
cursor = db.cursor()
sql = """SELECT * FROM states ORDERBY states.id"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
