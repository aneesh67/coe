import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="cvr",
)

cursor = mydb.cursor()

id=input("enter id")
yr=input("enter year")
name=input("enter cname")
mod=input("enter model")
cursor.execute("insert into car values(%s,%s,%s,%s)",(id,yr,name,mod))
mydb.commit()
