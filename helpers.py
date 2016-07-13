#!/usr/bin/env python

import ast # to parse text to python object
import os # to append to filenames
import csv

def importData(filename):
	results = []
	with open(filename, 'r') as f:
		for line in f:
			if len(line) > 2: # skip empty strings	
				results.append(ast.literal_eval(line))
	return results
	
def makeFileName(filename):
	name, ext = os.path.splitext(filename)
	return name + "change"
	
def runAlgorithm(filename, algorithm):
	problems = importData(filename)
	solutions = []
	for i in range(0,len(problems)-1,2): # go thru the list in pairs
		temp = algorithm(problems[i], problems[i+1])
		solutions.append(temp)
		solutions.append(sum(temp))
	with open(makeFileName(filename) + ".txt",'w') as f:
		f.write("Algorithm " + algorithm.__name__ + ":\n")
		for solution in solutions:
			f.write(str(solution) + '\n')
	f.close()

def doQuestion(filename, algorithm):
	problems = importData(filename)
	solutions = []
	for i in range(0,len(problems)-1,2): # go thru the list in pairs
		temp = algorithm(problems[i], problems[i+1])
		solutions.append([problems[i+1], sum(temp)])
	# WRITING TO CSV
	with open(makeFileName(filename) + "-" + algorithm.__name__ + ".csv", 'w') as f:
		writer = csv.writer(f, delimiter=',')
		for solution in solutions:
			writer.writerow(solution)
	f.close()
