#!/usr/bin/python

import sys
import csv
for line in sys.stdin:
	reader = csv.reader([line],skipinitialspace=True)
	sp_line = None
	for r in reader:
		sp_line = r
	country,country_code,region,region_code,city,date,download_kbps,upload_kbps,total_tests,distance_miles = sp_line
	print '{0}\t{1}'.format(country, download_kbps)