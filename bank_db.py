import mysql.connector as a
con=a.connect(
    host="localhost",
    user="root",
    passwd="####",
)
cursor=con.cursor()
db="create database bank"
cursor.execute(db)
use="use bank"
cursor.execute(use)
tb1="create table account( name varchar(50),pan varchar(25),dob varchar(25), phone varchar(15),addrs  varchar(250),opnblc integer,acount varchar(20) primary key)"
cursor.execute(tb1)
tb2="create table amount(name varchar(50),acount varchar(20) primary key,balance integer)"
cursor.execute(tb2)
print("Database Entered Successfully...")

