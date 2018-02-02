#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')
with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Heroes")

    for i in range(cur.rowcount):
        
        row = cur.fetchone()
        print row[0], row[1]
