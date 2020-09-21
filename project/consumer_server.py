# created separately to check if your kafka_server.py is working properly.
# make a screenshot
# https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html#kafka.KafkaConsumer

from kafka import KafkaConsumer
import json

class ConsumerServer(KafkaConsumer):
    def __init_(self, **kwargs):
        super().__init__(**kwargs)
    
    def run(self):
        for msg in self:
            print(msg.value)

if __name__ == "__main__":
    server = ConsumerServer(
        'com.github.leventarican.data',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='the-consumer-group',
        # Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    server.run()
