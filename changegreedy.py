#!/usr/bin/env python

import sys # for cli arguments
import helpers

def changegreedy(coins, amount):
	change = [0] * len(coins)
	while amount > 0:
		for idx,coin in reversed(list(enumerate(coins))):
			while (amount - coin) >= 0:
				amount -= coin
				change[idx] += 1
	return change
	
#-------------------------------------------------------------------------------
helpers.runAlgorithm(sys.argv[1], changegreedy)
