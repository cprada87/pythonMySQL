#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb 

def writeImage(data):
    
    fout = open('viuda2.jpg', 'wb')
    
    with fout:
        
        fout.write(data)

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores')
with con:

    cur = con.cursor()

    cur.execute("SELECT Data FROM Images WHERE Id=1")
    data = cur.fetchone()[0]
    writeImage(data)    
