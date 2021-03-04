import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
sql='CREATE TABLE student(sid VARCHAR(40),name VARCHAR(40),mark int)'
cursor.execute(sql)
#data=cursor.fetchone()
#print(data)