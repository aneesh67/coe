import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr",
)

cursor = mydb.cursor()

cursor.execute("select * from car")
st=cursor.fetchall()
for i in st:
    print(i)
mydb.commit()