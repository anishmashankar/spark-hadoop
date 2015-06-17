#!/usr/bin/python

import sys
import csv

oldKey = None
maxSpeed = 0.0
for line in sys.stdin:
	sp_line = line.strip().split('\t')
	thisKey, thisValue = sp_line
	if oldKey == thisKey:
		if maxSpeed < thisValue:
			maxSpeed = thisValue
	if oldKey and str(oldKey) != str(thisKey):
		print "{0},{1}".format(oldKey, maxSpeed)
		maxSpeed = 0
	oldKey = str(thisKey)