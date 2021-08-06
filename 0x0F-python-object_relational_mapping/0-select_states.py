#!/usr/bin/python
-- Create states table in hbtn_0e_0_usa with some data
import MySQLdb
from MySQLdb import _mysql


db = _mysql.connect(user="alx",passwd="1234",db="hbtn_0e_0_usa")
cursor = db.cursor()
sql = SELECT * FROM states ORDERBY states.id;
try:
    cursor.execute(sql);
    db.commit()
catch:
    db.rollback()
db.close()
