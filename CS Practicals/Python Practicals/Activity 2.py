#Activity 2

def isvowel():
	f = open("file1.txt")
	f1 = open("file2.txt", "a")
	a = f.read().split()
    for i in a:
        if a[0].lower not in "aeiou":
            f1.write(a)
        else:
            pass
    f.close()
    f1.close()

isvowel()