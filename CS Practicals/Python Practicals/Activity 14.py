#Activity 14

queue = []

def push(q, n):
    q.append(n)

#1
def addMember():
    dataInput = list(map(str,input().split()))
    push(queue, dataInput)

#2
def length():
    ln = 0
    for i in queue:
        ln += 1
    print('Length of queue is {}'.format(ln))

#3
def numberOfApplicants():
    d = {}
    for i in queue:
        if i[2] in d:
            d[i[2]] += 1
        else:
            d[i[2]] = 1
    for i in d:
        print('{} class has {} applicants'.format(i,d[i]))