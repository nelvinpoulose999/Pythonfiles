import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
delete_values='delete from student where sid="100"'
cursor.execute(delete_values)
#db.commit()