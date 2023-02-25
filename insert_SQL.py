import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(1549,'Anisha',9.54)")
mycursor.execute("insert into test1.test_table values(6598,'Karima',8.24)")
mycursor.execute("insert into test1.test_table values(5658,'Dhritikana',8.64)")
mycursor.execute("insert into test1.test_table values(5648,'Moumita',9.41)")
mydb.commit()
mydb.close()
