import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
update_values='UPDATE student set name="amal" where sid="100"'
cursor.execute(update_values)
db.commit()