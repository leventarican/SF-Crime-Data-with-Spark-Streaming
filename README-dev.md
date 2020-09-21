# ##############################################################################
# SF Crime Data with Spark Streaming

* __create__ a Kafka server to produce data, and __ingest__ data through Spark Structured Streaming.
* These starter code files should be edited:
```
producer_server.py
data_stream.py
kafka_server.py
```
* _optional_: create a consumer to test the kafka_server.py. ex. `consumer_server.py`
* create github repo: _If you complete the project in the classroom workspace here, just download the files you worked on and add them to your repo._

# project submit
* reviewer will be using this rubric to assess your project work: https://review.udacity.com/#!/rubrics/2676/view
> Here is what you need to submit for this project:
    > * A link to your GitHub repo.
    > * A zip file containing the three screenshots specified in steps 1 and 2 of the project directions

Please make sure you've included these three files in your GitHub repo:
```
producer_server.py
consumer_server.py
data_stream.py
```

> The `README.md` doc in your GitHub repo should also contain your responses to the two questions in step 3 of the project directions.

# ##############################################################################

# local environment
* given environment
```
Spark 2.4.3
Scala 2.11.x
Java 1.8.x
Kafka build with Scala 2.11.x
Python 3.6.x or 3.7.x
```
* ~~im using python3.8 ... lets see if this works~~
* use python3.7 with 3.8 this setup has issues.
```
TypeError: an integer is required (got type bytes)
```
* add python3.7 repo on ubuntu 20.04 then apt update, install
* also ensure to install venv lib
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.7
sudo apt install python3.7-dev python3.7-venv
```
* check JDK compatibility: https://docs.scala-lang.org/overviews/jdk-compatibility/overview.html
    * im using jdk 8 but jdk 11 should also work with scala 2.11.*. 
* download scala, spark, kafka. decompress
* create symbolic link, unlink
```
ln -s kafka_2.11-2.3.0 kafka

unlink kafka

spark -> spark-2.4.3-bin-hadoop2.7/
kafka -> kafka_2.11-2.3.0/
scala -> scala-2.11.12/
jdk -> zulu8.48.0.53-ca-jdk8.0.265-linux_x64/
```
* update your `.profile` file and reload
```
PATH="$HOME/development/jdk/bin:$PATH"
PATH="$HOME/development/kafka/bin:$PATH"
PATH="$HOME/development/scala/bin:$PATH"
PATH="$HOME/development/spark/bin:$PATH

source .profile
```
* __ignore__ `start.sh`. this is for conda. we will use virtual environment.
* setup virtual environment
```
cd project
python3.7 -m venv spark-env
source spark-env/bin/activate
pip3.7 install -r requirements.txt
```

* activate virtual environment
```
cd project
source spark-env/bin/activate
```

* deactivate virtual environment
```
deactivate
```

# begin
* start zookeeper `localhost:2181` and kafka broker `localhost:9092`
```
zookeeper-server-start.sh config/zookeeper.properties
    binding to port 0.0.0.0/0.0.0.0:2181

kafka-server-start.sh config/server.properties
    port 9092

kafka-topics.sh --list --zookeeper localhost
    default port 2182 is used

kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic com.github.leventarican.data --from-beginning

kafka-topics.sh --describe --zookeeper localhost:2181 --topic com.github.leventarican.data
```

# kafka python
* common python kafka libs
* kafka-python: https://kafka-python.readthedocs.io/en/master/
* PyKafka: https://pykafka.readthedocs.io/en/latest/
* confluent-kafka: https://docs.confluent.io/current/clients/confluent-kafka-python/

# spark-shell
* leave with CTRL+D
```
spark-shell
Spark context Web UI available at localhost:4040
Spark context available as 'sc' (master = local[*])
Spark session available as 'spark'
```

# issues
* use spark-sql-kafka-0-10_2.11:2.4.7 version 2.3.4 makes issues on my machine
* https://mvnrepository.com/artifact/org.apache.spark/spark-sql-kafka-0-10_2.11
```
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.7 --master local[*]
```
* mostly i received the following error
```
py4j.protocol.Py4JJavaError: An error occurred while calling o41.load.
: java.lang.NoClassDefFoundError: org/apache/spark/sql/sources/v2/reader/SupportsScanUnsafeRow
```
* ensure also that pyspark version matches with spark version
> Edit: to be more clear your PySpark version needs to be the same as the Apache Spark version that is downloaded, or you may run into compatibility issues
* https://stackoverflow.com/questions/53161939/pyspark-error-does-not-exist-in-the-jvm-error-when-initializing-sparkcontext
* use pip freeze to check current installation
```
pip freeze
```
