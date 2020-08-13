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

for t in range (int(input())):
	
