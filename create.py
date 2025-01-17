import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr",
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE car(id int,year int,cname int,model VARCHAR(100))")
mydb.commit()
