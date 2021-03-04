import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='collage'

)
cursor=db.cursor()
insert_values='INSERT INTO student(sid,name,mark) VALUES (%s,%s,%s)'
val=[
    ('100','ram',400),
    ('101','raj',350),
    ('102','rahul',300)
]
cursor.executemany(insert_values,val)
db.commit()