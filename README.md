
* __create__ a Kafka server to produce data, and __ingest__ data through Spark Structured Streaming.
* These starter code files should be edited:
```
producer_server.py
data_stream.py
kafka_server.py
```
* _optional_: create a consumer to test the kafka_server.py. ex. `consumer_server.py`
* create github repo: _If you complete the project in the classroom workspace here, just download the files you worked on and add them to your repo._

# local environment
* __ignore__ `start.sh`. this is for conda. we will use virtual environment.
* setup virtual environment
```
cd project
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

* activate virtual environment
```
cd python
. venv/bin/activate
```

* deactivate virtual environment
```
deactivate
