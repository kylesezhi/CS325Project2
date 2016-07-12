#!/usr/bin/env python

import ast # to parse text to python object
import os # to append to filenames

def importData(filename):
	results = []
	with open(filename, 'r') as f:
		for line in f:
			if len(line) > 2: # skip empty strings	
				results.append(ast.literal_eval(line))
	return results
	
def makeFileName(filename):
	name, ext = os.path.splitext(filename)
	return name + "change" + ext
	
def runAlgorithm(filename, algorithm):
	problems = importData(filename)
	solutions = []
	for i in range(0,len(problems)-1,2): # go thru the list in pairs
		temp = algorithm(problems[i], problems[i+1])
		solutions.append(temp)
		solutions.append(sum(temp))
	with open(makeFileName(filename),'w') as f:
		for solution in solutions:
			f.write(str(solution) + '\n')
	f.close()
