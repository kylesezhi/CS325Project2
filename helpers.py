#!/usr/bin/env python

import ast # to parse text to python object
import os # to append to filenames
import csv
import time

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
	timedata = [] # - Steven
	timeSum = 0
	for i in range(0,len(problems)-1,2): # go thru the list in pairs
		start = time.clock() # Time-related additions added later
		temp = algorithm(problems[i], problems[i+1])
		end = time.clock()
		speed = end - start
		timeSum = timeSum + speed
		timedata.append([problems[i+1], timeSum])
		solutions.append([problems[i+1], sum(temp)])
	# WRITING TO CSV
	with open(makeFileName(filename) + "-" + algorithm.__name__ + ".csv", 'w') as f:
		writer = csv.writer(f, delimiter=',')
		for solution in solutions:
			writer.writerow(solution)
	f.close()
	with open(makeFileName(filename) + "-" + algorithm.__name__ + "time" + ".csv", 'wb') as f:
		writer = csv.writer(f, delimiter=',')
		for line in timedata:
			writer.writerow(line)
	f.close()
