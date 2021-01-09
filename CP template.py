'''
Name: Devansh
Username: singhdevansh
Github: https://github.com/Devansh3712
'''

import os
import sys
import math
import itertools
from io import BytesIO, IOBase

#<fast I/O>
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
#</fast I/O>

#<template>
mod = (10**9)+7
pi = 3.14159265358979323846264338327950

def i1():	#int(input())
	return int(sys.stdin.readline())

def sf():	#input()
	return sys.stdin.readline()

def mi():	#map(int(input()))
	return map(int,sys.stdin.readline().split())

def arr():	#list(map(int,input().split()))
	return list(map(int,sys.stdin.readline().split()))

def pf(ans): #print(x)
	return sys.stdout.write(str(ans)+"\n")

def gcd(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
	if a > b:
		return gcd(a % b, b)
	else:
		return gcd(a, b % a)

def lcm(a, b):
	return (a * b) // gcd(a, b)
#</template>

#<testcases>
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
#</testcases>

#<solve>
def solve():

#</solve>

#<solution>
tc = i1()
for t in range (tc):
	solve()
#<solution>
