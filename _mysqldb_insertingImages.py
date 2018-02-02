#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb


def read_image():
    
    fin = open("viuda.jpg")    
    img = fin.read()
    
    return img
    

con = mdb.connect('localhost', 'nickFury', 'shield', 'vengadores') 
with con:
    
    cur = con.cursor()
    data = read_image()
    cur.execute("INSERT INTO Images VALUES(1, %s)", (data, ))
