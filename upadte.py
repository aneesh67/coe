import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr",
)

cursor = mydb.cursor()
cursor.execute("update car set cname='jai' where id=1")
mydb.commit()