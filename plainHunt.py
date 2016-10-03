#!/usr/bin/python

import sys

def hunt(change):
	for bell in range(1,len(change)-1,2):
		change[bell], change[bell+1] = change[bell+1], change[bell]
	print("".join(str(x) for x in change))
	return change

def cross(change):
	for bell in range(0,len(change)-2,2):
		change[bell], change[bell+1] = change[bell+1], change[bell]
	print("".join(str(x) for x in change))
	return change

def plainHunt(n):
	rounds = range(1,n+1)
	curChange = rounds
	print("".join(str(x) for x in curChange))
	for _ in range(0,2*n,2):
		cross(curChange)
		hunt(curChange)

if __name__ == "__main__":
   map(plainHunt, (int(x) for x in sys.argv[1:]))