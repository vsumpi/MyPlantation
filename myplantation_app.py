#!/usr/bin/env python3
# MyPlantation App 🌱

from os import curdir
import sqlite3

# Inicialization 🚀
print("Connect:", end="\rConnect:")
con = sqlite3.connect("myfarm.db")
print("OK")
print("Create:", end="\rCreate:")
print("OK")
cur = con.cursor()


# Create table for user ➕ (multiuser support)
def make():
    cur.execute(table)
    con.commit()

# Register a plant with 3 input values and insert into the user's table
def registerNewPlant():
    plantDate = input("Enter when the plant was planted:")
    storageId = input("Enter which storage is it in: ")
    plantType = input("Enter what plant is it:")
    newPlant = f"INSERT INTO {username}(planted, storageid, type) VALUES('{plantDate}',{storageId},\"{plantType}\");"
    cur.execute(newPlant)
    con.commit()


print("Please enter your username:")
username = input()
table = f"CREATE TABLE IF NOT EXISTS {username} (ID INTEGER PRIMARY KEY AUTOINCREMENT, planted date, lastirrigation date, storageid integer, type text);"
make()

# Activities 🧩
print("Activities:\n\t1. Register a new plant")
registerNewPlant()
#res = cur.execute("SELECT * FROM sumpi")
#for item in res.fetchall():
#    print(item)