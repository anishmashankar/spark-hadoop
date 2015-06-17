from pyspark import SparkContext
import csv
def mapper(line):
	'''try:
		unicode(line,'ascii')
	except:
		line = unicode(line, 'utf-8')'''
	reader = csv.reader([line],skipinitialspace=True)
	sp_line = None
	for r in reader:
		sp_line = r
	country,country_code,region,region_code,city,date,download_kbps,upload_kbps,total_tests,distance_miles = r
	return country, download_kbps
	#print len(sp_line)

def reducer(a,b):
	if a>b:
		return a
	else:
		return b

speeds_file = "/user/anish/indata/filtered_speeds.csv"

sc = SparkContext('local','NetIndex')

speeds = sc.textFile(speeds_file).map(mapper).reduceByKey(reducer).collect()
print speeds