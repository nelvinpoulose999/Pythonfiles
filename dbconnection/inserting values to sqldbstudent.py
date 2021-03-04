import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
insert_values='INSERT INTO student VALUES("100","ram",400)'
cursor.execute(insert_values)
db.commit()