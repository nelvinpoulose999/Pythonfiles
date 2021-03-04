import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
read_values='select * from student'
cursor.execute(read_values)
data=cursor.fetchall()
print(data)