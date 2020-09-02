import csv
file=open("students.csv","r")
obj=csv.reader(file.delimiter='\t')

#1

def copyIntoTuple():
    listOfStudents=[]
    for i in obj:
        listOfStudents.append(tuple(obj))
    print(listOfStudents)
copyIntoTuple()

#2

#Names of students with no. of year < 3
def numOfYear():
    for i in obj:
        if int(i['no of years'])<3:
            print(i['firstname'],i['lastname'])
numOfYear()

#Number of people in each department
def numOfstd():
    d={}
    for i in obj:
        if i['department'] in d:
            d[i['department']]+=1
        else:
            d[i['department']]=1
    for i in d:
        print('{}: {}'.format(i,d[i]))
numOfstd()

