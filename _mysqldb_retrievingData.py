#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Heroes")

    rows = cur.fetchall()

    for row in rows:
        print row

