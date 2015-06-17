import sys
import csv
count=0
with open("filtered_speeds.csv",'w+') as ofile:
	for line in sys.stdin:
		count+=1
		sys.stdout.write("line"+str(count)+'\r')
		sys.stdout.flush()
		try:
			x = unicode(line)
			ofile.write(line)
		except:
			continue