#Activity 4

f = open("myfile.txt")
x = f.read().split()

d = {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(len(x))
print(len(d))

c = ''
e = 0
for i in d:
    if d[i] > e:
        e = d[i]
        c = i
a = d.get(key = c)
print(a)

def find_longest_word():
    s = ''
    g = 0
    for i in d:
        if len(i) > g:
            g = len(i)
            s = i
    return s
print(find_longest_word())

n = int(input("Enter a number: "))
def filter_long_words(n):
    l = []
    for i in d:
        if len(i) > n:
            l.append(i)
    return l
print(filter_long_words(n))

f.close()