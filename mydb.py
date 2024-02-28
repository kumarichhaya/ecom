import mysql.connector

dataBase =mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'awesome',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE devpharma")
print("all done")
