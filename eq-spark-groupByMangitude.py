from pyspark import SparkConf, SparkContext 
import collections 

conf = SparkConf().setMaster("local").setAppName("EarthquakesHistogram") 
sc = SparkContext(conf = conf) 

def parseLine(line):
	fields = line.split(',')
	mag = float(fields[8])
	return mag

lines = sc.textFile("hdfs:///user/maria_dev/earthquakes-final.csv")
rdd = lines.map(parseLine) 
result = rdd.countByValue() 

sortedResults = collections.OrderedDict(sorted(result.items())) 
for key, value in sortedResults.items(): 
	print("%s %i" % (key, value))

