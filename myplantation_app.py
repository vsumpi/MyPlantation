#!/usr/bin/env python
# MyPlantation App 🌱
# Just updated: SQLite -> MariaDB SQL 2024.01.15 16:01

from os import curdir
import pymysql

# Inicialization 🚀
# Source:https://pymysql.readthedocs.io/en/latest/user/examples.html
# Connect to the database

connection = pymysql.connect(host='localhost',
                             user='pythonapi',
                             password='admin',
                             database='myplantationdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
"""
with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('pythonapi', 'admin'))
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('pythonapi'))
        result = cursor.fetchone()
        print(result)
"""


#  Create table for user ➕ (multiuser support)
def make():
    with connection.cursor() as cursor:
        cursor.execute(table)
        connection.commit()

# Register a plant with 3 input values and insert into the user's table
def registerNewPlant():
    with connection.cursor() as cursor:
        plantDate = input("Enter when the plant was planted:")
        storageId = input("Enter which storage is it in: ")
        plantType = input("Enter what plant is it:")
        newPlant = f"INSERT INTO {username}(planted, storageid, type) VALUES('{plantDate}','{storageId}','{plantType}');"
        cursor.execute(newPlant)
        connection.commit()


print("Please enter your username:")
username = input()
table = f"CREATE TABLE IF NOT EXISTS {username}(ID INTEGER PRIMARY KEY AUTO_INCREMENT, planted DATE, lastirrigation DATE, storageid INTEGER, type TEXT);"
make()

# Activities 🧩
print("Activities:\n\t1. Register a new plant")
registerNewPlant()
#res = cur.execute("SELECT * FROM sumpi")
#for item in res.fetchall():
#    print(item)
with connection.cursor() as cursor:
    cursor.close()
    connection.close()