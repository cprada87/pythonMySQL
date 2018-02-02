#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')
with con:

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Heroes LIMIT 11")

    rows = cur.fetchall()

    for row in rows:
        print row["Id"], row["Name"]
