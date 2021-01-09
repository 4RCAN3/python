#Activity 4 (Connectivity)

from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
from tabulate import tabulate

connectMySQL = mc.connect(host = 'localhost', user = 'root', password = 'root', database = 'mydb')

cursor = connectMySQL.cursor(buffered = True)

def print_table():
	cursor.execute("select * from BUS")
	result = cursor.fetchall()
	return tabulate(result, headers = ['BusNo', 'Origin', 'Dest', 'Rate', 'Km'], tablefmt = 'psql')

def show_details():
	new = Toplevel(root)
	new.title("Details")
	textbox = Text(new, height = 20, width = 60)
	table = print_table()
	textbox.insert(INSERT, table)
	textbox.config(state = "disabled")
	textbox.grid(row = 0)

def add_record():
	new = Toplevel(root)
	new.title("Add Record")
	new.resizable(False, False)

	bus_no = StringVar(new)
	origin = StringVar(new)
	dest = StringVar(new)
	rate = StringVar(new)
	km = StringVar(new)

	label_bus_no = Label(new, text = "BusNo")
	entry_bus_no = Entry(new, textvariable = bus_no)
	label_origin = Label(new, text = "Origin")
	entry_origin = Entry(new, textvariable = origin)
	label_dest = Label(new, text = "Dest")
	entry_dest = Entry(new, textvariable = dest)
	label_rate = Label(new, text = "Rate")
	entry_rate = Entry(new, textvariable = rate)
	label_km = Label(new, text = "KM")
	entry_km = Entry(new, textvariable = km)

	def insert_value_db():
		nonlocal bus_no, origin, dest, rate, km
		b = int(bus_no.get())
		o = origin.get()
		d = dest.get()
		r = int(rate.get())
		k = int(km.get())
		sql = f"insert into BUS values({b}, '{o}', '{d}', {r}, {k})"
		cursor.execute(sql)
		connectMySQL.commit()
		messagebox.showinfo("Information", "Record added successfully!")
		new.destroy()

	label_bus_no.grid(row = 0, column = 0)
	entry_bus_no.grid(row = 0, column = 1)
	label_origin.grid(row = 1, column = 0)
	entry_origin.grid(row = 1, column = 1)
	label_dest.grid(row = 2, column = 0)
	entry_dest.grid(row = 2, column = 1)
	label_rate.grid(row = 3, column = 0)
	entry_rate.grid(row = 3, column = 1)
	label_km.grid(row = 4, column = 0)
	entry_km.grid(row = 4, column = 1)
	button_submit = Button(new, text = "Submit", command = insert_value_db)
	button_submit.grid(row = 5, columnspan = 2)

root = Tk()
root.title("Bus Records")

label1 = Label(root, text = "Bus Records")
button_show_details = Button(root, text = "Details", command = show_details)
button_add_record = Button(root, text = "New Record", command = add_record)

label1.grid(row = 0, columnspan = 2)
button_show_details.grid(row = 1, column = 0)
button_add_record.grid(row = 1, column = 1)
root.mainloop()