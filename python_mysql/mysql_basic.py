# MySql 8.0 이상 유저
#pip install mysql-connector-python

# 하위 버전
#pip install mysql.connector

import mysql.connector


#MYSQL에 연결하기
'''
mydb = mysql.connector.connect(host="localhost", user='*********', password='*********')
#print(mydb) # <mysql.connector.connection_cext.CMySQLConnection object at 0x7f1a45eda910>
'''

#DB 만들기
'''
mycursor = mydb.cursor()
mycursor.execute("create database mydb");
'''

#만들어졌는지 확인하기
'''
mycursor.execute("show databases")

for x in mycursor:
    print(x)
'''

# DB 존재시, DB에 바로 접근하기
mydb = mysql.connector.connect(host="localhost", user='jinsu9758', password='!Cowlstn0208', database="mydb")

#Table 만들기
mycursor = mydb.cursor()

#print(mycursor)
'''
mycursor.execute("create table customer (name varchar(255), address varchar(255))")
'''

#Table 생성 확인하기

mycursor.execute("show tables")
for x in mycursor:
    print(x)
