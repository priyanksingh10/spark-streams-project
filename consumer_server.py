from kafka import KafkaConsumer
import json
import time


class ConsumerServer:

    def consume_data(self, consumer):
        for msg in consumer:
            if msg is None:
                print(f"No message received")
            else:
                print(f"Received message: {msg.value.decode('utf-8')}")
        

if __name__ == "__main__":
    
    consumer_server = ConsumerServer()
    consumer = KafkaConsumer(
                "org.sfo.pod.svc.calls",
                bootstrap_servers="localhost:9092",
                client_id="pod-svc-calls-1-consumer",
                group_id="consumer-grp-1")
    
    consumer_server.consume_data(consumer)