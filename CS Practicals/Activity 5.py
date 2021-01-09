#Activity 5

import pickle as pk
import os

d = {}
def write():
    f = open("hotel.dat","ab")
    n = int(input("Enter the number of entries: "))
    for i in range (n):
        d["roomno"] = input("Enter room number: ")
        d["name"] = input("Enter name: ")
        d["duration"] = input("Enter the duration of stay: ")
        pk.dump(d, f)
    f.close()
    print("Data recorded succesfully.\n")

def read():
    f = open("hotel.dat","rb")
    try:
        while (True):
            obj = pk.load(f)
            print(obj)
    except EOFError:
        f.close()
        pass

def readspecific():
    f = open("hotel.dat","rb")
    n = input("Enter the room number: ")
    flag = False
    try:
        while (True):
            obj = pk.load(f)
            if obj["roomno"] == n:
                print(obj)
            flag = True
    except EOFError:
        f.close()
        pass
    if flag == False:
        print("Record not found\n")

def modify():
    f = open("hotel.dat","rb")
    f1 = open("new.dat","ab")
    n = input("Enter the room number: ")
    flag = False
    try:
        while (True):
            obj = pk.load(f)
            if obj["roomno"] == n:
                obj["duration"] = input("Enter the new duration: ")
                pk.dump(obj, f1)
            else:
                pk.dump(obj, f1)
            flag=True
    except EOFError:
        f.close()
        f1.close()
        pass
    os.remove("hotel.dat")
    os.rename("new.dat", "hotel.dat")
    if flag == False:
        print("Record not found\n")
    else:
        print("Record modified successfully\n")

def delete():
    f = open("hotel.dat","rb")
    f1 = open("new.dat","ab")
    n = int(input("Enter the room number you want to delete: "))
    flag = False
    try:
        while (True):
            obj = pk.load(f)
            if obj["roomno"] == n:
                pass
            else:
                pk.dump(obj, f1)
            flag = True
    except EOFError:
        f.close()
        f1.close()
        pass
    os.remove("hotel.dat")        
    os.rename("new.dat", "hotel.dat")
    if flag == False:
        print("Record not found\n")
    else:
        print("Record deleted successfully\n")

while (True):
    print(">>>Welcome to hotel database<<<\n")
    print("1. Write a new entries")
    print("2. Read all the entries")
    print("3. Read a specific entry")
    print("4. Modify an entry")
    print("5. Delete an entry")
    print("6. Exit")
    v = int(input("Enter your choice: "))
    if v == (1):
        write()
    elif v == (2):
        read()
    elif v == (3):
        readspecific()
    elif v == (4):
        modify()
    elif v == (5):
        delete()
    elif v == (6):
        print("Program is terminating.")
        break
    else:
        print("Enter the correct input")