#!/usr/bin/python

import sys
import re

def pnRegularizer(pNote,stage):
	if stage == "E" or stage == "e":
		stageN = 11
	elif stage == "T" or stage == "t":
		stageN = 12
	else:
		stageN = int(stage)

	pNote = pNote.replace("e","E")
	pNote = pNote.replace("t","T")
	pNote = pNote.replace("h","1.")
	pNote = re.sub(r'([et\d])(?=[xh-])', r'\g<0>.', pNote)
	if stageN%2==0:
		pNote = re.sub(r'[x-]', "x.", pNote)
		pNote = re.sub(r'([13579E])(?=\.)', r'\g<0>'+stage, pNote)
	else:
		pNote = re.sub(r'[x-]', stage+".", pNote)
		pNote = re.sub(r'([24680T])(?=\.)', r'\g<0>'+stage, pNote)
	pNote = re.sub(r'(?<=[^\dET])([24680T])', r'1\g<1>', pNote)
	pNote = re.sub(r'^([24680T])', r'1\g<1>', pNote)

	pNote = re.sub(r'\.*(?=[\s\b])', "", pNote)

	return pNote


def notationReader(pNote,stage):
	if stage == "E":
		stageN = 11
	elif stage == "T":
		stageN = 12
	else:
		stageN = int(stage)
	rounds = list(range(1,stageN+1))
	curChange = list(range(1,stageN+1))
	pNote = pNote.split()
	lead = re.sub(r'([et\d])(?=[xh-])', r'\g<0>.', pNote[0])
	if stageN%2==0:
		lead = lead.replace("h","1"+str(stage)+".")
		lead = re.sub(r'[x-]', r'x.', lead)
	else:
		lead = lead.replace("h","1.")
		lead = re.sub(r'[x-]', "1.", lead)

	if len(pNote)>1:
		lead += ".".join(lead[:-1].split(".").reverse()) + pNote[1][1:]
	else:
		lead = lead.rstrip(".")
	print(lead)

if __name__ == "__main__":
   # notationReader(str(sys.argv[1]),str(sys.argv[2]))
	print(pnRegularizer(str(sys.argv[1]),str(sys.argv[2])))