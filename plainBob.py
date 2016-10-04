#!/usr/bin/python

import sys

def hunt(change):
	for bell in range(1,len(change)-1,2):
		change[bell], change[bell+1] = change[bell+1], change[bell]
	print("".join(str(x) for x in change))
	return change

def cross(change):
	for bell in range(0,len(change)-1,2):
		change[bell], change[bell+1] = change[bell+1], change[bell]
	print("".join(str(x) for x in change))
	return change

def seconds(change):
	for bell in range(2,len(change)-1,2):
		change[bell], change[bell+1] = change[bell+1], change[bell]
	print("".join(str(x) for x in change))
	return change

def plainBob(n):
	rounds = range(1,n+1)
	curChange = range(1,n+1)
	print("".join(str(x) for x in curChange))
	while True:
		cross(curChange)
		if curChange[0] == 1:
			seconds(curChange)
		else:
			hunt(curChange)
		if curChange == rounds:
			break
			

if __name__ == "__main__":
   map(plainBob, (int(x) for x in sys.argv[1:]))