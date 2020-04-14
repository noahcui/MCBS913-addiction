#!/usr/bin/python

import sys
import sqlite3

def create_table(c, table_name):
    cmd = "create or replace table " + table_name + "(INFO,text\
        SEQ text,\
        START int,\
        END int);"
    c.execute(cmd)
    print("table created successfully, now inserting datas")

def insert_data(c, table_name, data):
    cmd = "INSERT INTO " + table_name + "(INFO, SEQ, START, END) VALUES (?,?,?,?);"
    c.execute(cmd, data)

if __name__ == '__main__':
    conn = None
    dbname = sys.argv[1]
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    table_name = sys.argv[2]
    create_table(c, table_name)
    for i in range(len(sys.argv)):
        if i > 2:
            #directiory
            file_name = sys.argv[i]
            c = 0
            with open(file_name, "r") as pos_file:
                for line in pos_file:
                    if c % 5 == 0:
                        File = line.replace('File: ', '')
                        c = c + 1
                    if c % 5 == 1:
                        Query = line.replace('Query: ', '')
                        c = c + 1
                    if c % 5 == 2:
                        Reference = line.replace('Reference: ', '')
                        c = c + 1
                    if c % 5 == 3:
                        Position = line.replace('Position: ', '')
                        c = c + 1
                    else:
                        data = (File, Query, Reference, Position)
                        insert_data(c, table_name, data)
    conn.commit()
    conn.close()