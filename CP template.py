import atexit, io, sys

#buffer io template begins
buffer=io.BytesIO()
sys.stdout=buffer

@atexit.register
def write():
	sys.__stdout__.write(buffer.getvalue().decode('utf-8'))
#buffer io template ends

sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

def sums(arr):
	s=0
	for i in arr:
		s=s+i
	return s 

for t in range (int(input())):
	