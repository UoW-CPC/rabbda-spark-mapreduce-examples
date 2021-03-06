# rabbda-spark-mapreduce-examples

## Getting started

First open a terminal and download the repository:
```
git clone https://github.com/UoW-CPC/rabbda-spark-mapreduce-examples.git
```
Move to the repository:
```
cd rabbda-spark-mapreduce-examples
```
There you can see two folders:
* earthquakes - Part A
* movies - Part B

## Part A – Analysing Earthquakes data with Spark and PySpark

Move to the earthquakes folder:
```
cd earthquakes
```
in that folder you can find 4 files:
* earthquakes.csv - Sample data
* eq-spark-groupByMangitude.py - Spark script
* eq-spark-groupByYear.py - Spark script
* eq-spark-sql-groupByCountry.py - Spark script

Initialy you need to upload the sample data to HDFS:
```
# command hdfs dfs –put earthquakes.csv /YOUR_HDFS_PATH
# sample command for Hortonwork Data Platform with user maria_dev
hdfs dfs -put earthquakes.csv /user/maria_dev/earthquakes.csv
```

See the file in HDFS:
```
hdfs dfs -ls /user/maria_dev/
```

Now we are ready to run the spark scripts:

__Notice:__ In case you are not using HDP with user maria_dev, please change the HDFS path in those script accordingly.

1.	Group earthquakes by year with spark:
```
spark-submit eq-spark-groupByYear.py
```
Output:
```
2018 180755
2019 154527
```
2.	Group earthquakes by magnitude with spark:
```
spark-submit eq-spark-groupByMangitude.py
```
Sample output:
```
6.4 24
6.5 13
6.6 11
6.7 9
6.8 9
6.9 6
7.0 3
7.1 7
7.2 1
7.3 4
7.5 5
7.6 1
7.9 2
8.0 1
8.2 1
```
3.	Group earthquakes by country with spark sql:
```
spark-submit eq-spark-sql-groupByCountry.py
```

Sample output:
```
|"101km W of Honiara                   |1    |
|"101km W of Iwanai                    |1    |
|"101km W of Kuqa                      |1    |
|"101km W of Larsen Bay                |1    |
|"101km W of Mendi                     |1    |
|"101km W of Old Crow                  |1    |
|"101km W of Ovalle                    |1    |
|"101km W of San Antonio de los Cobres |1    |
|"101km W of Tarauaca                  |1    |
|"101km W of Willow                    |10   |
|"101km WNW of Arctic Village          |6    |
|"101km WNW of Cantwell                |2    |
|"101km WNW of Chirikof Island         |2    |
|"101km WNW of Gustavus                |1    |
```

Move back to the parent folder:
```
cd ..
```

## Part B – Analysing Movies data with Map-Reduce, Spark with Python scripts

Move to the movies folder:
```
cd movies
```
in that folder you can find 4 files:
* movies.txt - Sample data
* users.txt - Sample data
* ratings.py - MR job script
* worst_movies.py - Spark script

Initialy you need to upload the sample data usets.txt to HDFS:
```
# command hdfs dfs –put users.txt /YOUR_HDFS_PATH
# sample command for Hortonwork Data Platform with user maria_dev
hdfs dfs -put users.txt /user/maria_dev/users.txt
```

See the file in HDFS:
```
hdfs dfs -ls /user/maria_dev/
```

The file movies.txt will be access for the local filesystem.

Now we are ready to run the scripts:

__Notice:__ In case you are not using HDP with user maria_dev, please change the HDFS path in the script worst_movies.py accordingly.

First we will try to submit an MR job to analyse the ratings in the user.txt.
Before we execute the script we need to install the python mrjob package, otherwise the execution will fail.
To do so run:
```
sudo yum install python-pip
```
```
sudo pip install mrjob
```

We can run the MR Job in two ways:
* Locally:
```
python ratings.py users.txt
```
Output:
```
"4"	34174
"3"	27145
"1"	6111
"2"	11370
"5"	21203
````

* On the Hadoop cluster:
```
python ratings.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar users.txt
```
Output:
```
"1"	6111
"2"	11370
"3"	27145
"4"	34174
"5"	21203
````

Run both and compare execution time and messages.


Now let's try to submit a Spark Job to find the worst movies by joining the two datasets movies.txt and users.txt.

To submit the python script run the following:
```
spark-submit worst_movies.py
```
Output:
```
('3 Ninjas: High Noon At Mega Mountain (1998)', 1.0)
('Beyond Bedlam (1993)', 1.0)
('Power 98 (1995)', 1.0)
('Bloody Child, The (1996)', 1.0)
('Amityville: Dollhouse (1996)', 1.0)
('Babyfever (1994)', 1.0)
('Homage (1995)', 1.0)
('Somebody to Love (1994)', 1.0)
('Crude Oasis, The (1995)', 1.0)
('Every Other Weekend (1990)', 1.0)
```




