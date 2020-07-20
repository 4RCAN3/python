f=open("file1.txt")
f1=open("file2.txt","a")
a=f.read().split()
def isvowel():
    for i in a:
        if a[0].lower not in "aeiou":
            f1.write(a)
        else:
            pass
isvowel()