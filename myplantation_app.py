#!/usr/bin/python
# MyPlantation App 🌱
# Copyright(c) Varga "vsumpi" Zsombor, 2024

import os
import time
import pymysql
from os import curdir
from dotenv import load_dotenv


# 📜 Setting .env variables
load_dotenv(dotenv_path="./development.env")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
CHARSET = os.getenv("CHARSET")

# 🔗 Init Database connection
connection = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE,
    charset=CHARSET,
    cursorclass=pymysql.cursors.DictCursor,
)
with connection.cursor() as cursor:
    pass


# 💁 Multiuser support
# Creating a DB Table for every user
def createSQLTableForUser(username):
    table = f"CREATE TABLE IF NOT EXISTS {username}(ID INTEGER PRIMARY KEY AUTO_INCREMENT, planted DATE, lastirrigation DATE, storageid INTEGER, type TEXT);"
    with connection.cursor() as cursor:
        cursor.execute(table)
        connection.commit()


# 🌱 Creating a Plant
class Plant:
    def __init__(self, plantDate, storageId, plantType):
        self.plantDate
        self.storageId
        self.plantType


# 🔧 Construct the Plant
def plantData():
    Plant.plantDate = input("Enter WHEN the plant was planted:")
    Plant.storageId = input("Enter WHICH storage is it in: ")
    Plant.plantType = input("Enter WHAT plant is it:")


# 📦 Delivering the 🌱 Plant to the 💁 User
def plantToUser(username):
    newPlant = f"INSERT INTO {username}(planted, storageid, type) VALUES('{Plant.plantDate}','{Plant.storageId}','{Plant.plantType}');"
    with connection.cursor() as cursor:
        cursor.execute(newPlant)
        connection.commit()


# 🎨 Design
def screenStart():
    print("START OK")
    time.sleep(1)
    os.system("cls")
    print("#################")
    print("# W E L C O M E #")
    print("#################")
    time.sleep(2)
    os.system("cls")


#  🚀 MAIN 🚀
#  Enter your code to run here:
if __name__ == "__main__":
    screenStart()
    print("Please enter your username:")
    username = input()
    createSQLTableForUser(username)
    plantData()
    plantToUser(username)

    #  END NOTE! These MUST be the last lines in the code!
    cursor.close()
    connection.close()
