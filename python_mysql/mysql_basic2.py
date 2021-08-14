import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="*********", password="*********", database="mydb")

mycursor = mydb.cursor()


#Insert 쿼리 예제 실습하기
'''
sql = "INSERT INTO customer(name, address) VALUES(%s, %s)"

val = ('John', 'Highway 21')

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
'''

#Insert Multiple rows
'''
sql = "insert into customer(name, address) values(%s, %s)"
val = [('Peter', 'Lowstreet 4'), ('Amy', 'Apple st 652'),('Hannah','Mountain 21')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")
'''

#Select 레코드 조회하기
'''
mycursor.execute("select * from customer")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
'''

#delete 레코드 삭제하기
sql = "delete from customer where address='Mountain 21'"
mycursor.execute(sql)
mydb.commit()

