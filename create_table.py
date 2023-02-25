import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT, c2 VARCHAR(50), c3 FLOAT)")
mydb.close()