#Activity 3 (Connectivity)

import mysql.connector as mc
connectMySQL = mc.connect(host = 'localhost', user = 'root', password = 'root', database = 'mydb')

cursor = connectMySQL.cursor(buffered = True)

def insert_values():
	roll_no = int(input("Enter RollNo: "))
	name = input("Enter Name: ")
	u_class = int(input("Enter Class: "))
	dob = input("Enter DOB in DD-MM-YYYY format: ")
	gender = input("Enter Gender: ")
	sql = f"insert into STUDENT values({roll_no}, '{name}', {u_class}, '{dob}', '{gender}')"
	cursor.execute(sql)
	connectMySQL.commit()

def update_values():
	roll_no = int(input("Enter RollNo: "))
	values = ['name', 'u_class', 'dob', 'gender']
	print(f'Available attributes to update are: {values}')
	user_input = input("Enter value to be updated: ")
	if user_input.lower() in values:
		if user_input.lower() == 'name':
			name = input("Enter Name: ")
			sql = f"update STUDENT set Name = '{name}' where RollNo = {roll_no}"
			cursor.execute(sql)
		elif user_input.lower() == 'u_class':
			u_class = int(input("Enter Class: "))
			sql = f"update STUDENT set Class = {u_class} where RollNo = {roll_no}"
			cursor.execute(sql)
		elif user_input.lower() == 'dob':
			dob = input("Enter DOB in DD-MM-YYYY format: ")
			sql = f"update STUDENT set DOB = '{dob}' where RollNo = {roll_no}"
			cursor.execute(sql)
		else:
			gender = input("Enter Gender: ")
			sql = f"update STUDENT set DOB = '{dob}' where RollNo = {roll_no}"
			cursor.execute(sql)
		print("Data succesfully updated")
	else:
		print("No such attribute in table")
	connectMySQL.commit()