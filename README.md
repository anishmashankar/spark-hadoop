# spark-hadoop
A simple application created to test the performance of [spark](http://spark.apache.org) and traditional map reduce on a Pseudo Distributed [Hadoop](http://hadoop.apache.org) cluster. The dataset used is download from [NetIndex](http://netindex.com). For the scope of this project, extract the dataset zip to this project folder

## Perform the test on your own?
I have taken the file **city_speeds_daily.csv** which sized to 2.4GB. Some kind of wrangling had to be done to maintain the simplicity of the project. The problems regarding encoding were taken care by the file *eliminate_malformed_data.py*. It is a humble request that you execute the file as following

```sh
cat city_daily_speeds.csv | python eliminate_malformed_data.py
```

This creates a new file called filtered_speeds.csv, which is free of all encoding problems. Now, all we have to do is copy the file to the hadoop cluster. Make sure it is running and execute the following after you are in the hadoop root folder

```sh
bin/hdfs dfs -copyFromLocal /local/path/to/netindex/filtered_speeds.csv \ 
/user/awesome/indata/filtered_speeds.csv
```
Now that the data exists in the cluster, we are ready to perform analysis.

Run the hadoop map reduce job using the [streaming api](https://hadoop.apache.org/docs/r2.7.0/hadoop-streaming/HadoopStreaming.html). 

```sh
bin/hadoop jar /path/to/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-input /user/anish/indata -out /user/anish/outputdir3 \
-mapper /home/anish/Documents/DataSets/netindex/map.py \
-reducer /home/anish/Documents/DataSets/netindex/reduce.py \
-file /home/anish/Documents/DataSets/netindex/map.py \
-file /home/anish/Documents/DataSets/netindex/reduce.py
```

Wait for the job to finish.

Lets try running the spark application now.

First, check the file sparking.py. Find the definition of the variable *speeds_file*
```python
speeds_file = "/user/anish/indata/filtered_speeds.csv"
```
Edit this value so that it points exactly to the filtered_speeds.csv we have copied from local storage.

Now, execute
```sh
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop \
bin/spark-submit --master yarn /path/to/sparking.py 
```
For me, it took around 4.30 minutes on the map reduce and 3.15 minutes on the spark application.
