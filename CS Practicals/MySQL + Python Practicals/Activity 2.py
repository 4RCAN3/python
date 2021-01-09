#Activity 2 (Connectivity)

import mysql.connector as mc
connectMySQL = mc.connect(host = 'localhost', user = 'root', password = 'root', database = 'mydb')

cursor = connectMySQL.cursor(buffered = True)

def insert_values():
	item_code = input("Enter the ItemCode: ")
	item_name = input("Enter the ItemName: ")
	price = float(input("Enter the Price: "))
	sql = f"insert into ITEM values ('{item_code}', '{item_name}', {price})"
	cursor.execute(sql)
	connectMySQL.commit()

def display_records():
	sql = "select * from ITEM"
	cursor.execute(sql)
	result = cursor.fetchall()
	for i in result:
		print(i)

def search():
	item_code = input("Enter the ItemCode: ")
	sql = "select * from ITEM where Itemcode = '{item_code}'"
	cursor.execute(sql)
	result = cursor.fetchone()
	print(result)