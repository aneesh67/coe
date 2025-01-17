import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr",
)

cursor = mydb.cursor()
cursor.execute("select * from car where id between 1 and 3")
res=cursor.fetchall()
for s in res:
    print(s)
mydb.commit()