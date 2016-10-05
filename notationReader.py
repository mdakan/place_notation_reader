#!/usr/bin/python

import sys
import re

def notationReader(pNote,stage):
	rounds = list(range(1,stage+1))
	curChange = list(range(1,stage+1))
	pNote = pNote.split()
	lead = re.sub(r'(\d)(?=[xh-])', r'\g<0>.', pNote[0])
	lead = re.sub(r'[x-]', r'.', lead)
	lead = lead.replace("h","1"+str(stage)+".")

	if len(pNote)>1:
		lead.append(pNote[1][-1])
	else:
		lead = lead.rstrip(".")
	print(lead)

if __name__ == "__main__":
   notationReader(str(sys.argv[1]),int(sys.argv[2]))