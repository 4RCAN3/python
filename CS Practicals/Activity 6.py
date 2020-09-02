import csv
file=open('placement.csv','r')
obj=csv.reader(file)

#print the data
for i in obj:
    print(i)

#total number of people who came for the test
def numOfPeople():
    c=0
    for i in obj:
        if i['NAME'] not None:
            c+=1
    print('{} people came for the placement test'.format(c))
numOfPeople()

#top n names on basis of total marks
def totalMarks():
    top=0
    for i in obj:
        total=0
        total+=int(i['MARKS 1'])+int(i['MARKS 2'])+int(i['MARKS 3'])+int(i['MARKS 4'])+int(i['MARKS 5'])
        top=max(top,total)
        if total>=top:
            print(i['NAME'])
totalMarks()

