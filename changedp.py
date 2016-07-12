#!/usr/bin/env python

# m is size of coins array (number of different coins)
import sys
import helpers

def changedp(coinValueList,change):

  coinsUsed = [0]*(change+1)
  minCoins = [0]*(change+1)
  usedArr = []
  coinTally = []

  for cents in range(change+1):
    coinCount = cents
    newCoin = 1

    for j in [c for c in coinValueList if c <= cents]:
      if minCoins[cents-j] + 1 < coinCount:
        coinCount = minCoins[cents-j]+1
        newCoin = j

    minCoins[cents] = coinCount
    coinsUsed[cents] = newCoin

  coin = change

  while coin > 0:
    thisCoin = coinsUsed[coin]
    usedArr.append(thisCoin)
    coin = coin - thisCoin

  for i in coinValueList:
    coinTally.append(usedArr.count(i))

  return coinTally

#-------------------------------------------------------------------------------
helpers.runAlgorithm(sys.argv[1], changedp)
