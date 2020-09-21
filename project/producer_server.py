from kafka import KafkaProducer
import json
import time

#
# You Need to Edit in Your Project Work
#

# https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html

# kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic com.github.leventarican.data --from-beginning

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic
        # self.valueserializer = lambda v: json.dumps(v).encode('utf-8')

    #TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            # Deserialize a file-like object containing a JSON document to a Python object (JSONDecoder)
            obj = json.load(f)
            for line in obj:
                message = self.dict_to_binary(line)
                # TODO send the correct data
                self.send(self.topic, value=message)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary
    # Serialize obj to a JSON formatted str.
    # encode will return bytes
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
