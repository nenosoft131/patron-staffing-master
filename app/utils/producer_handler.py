from confluent_kafka import Producer

class KafkaProducer:
    def __init__(self, broker: str, topic: str):
        self.producer = Producer({"bootstrap.servers": broker})
        self.topic = topic

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def send_message(self, key: str, value: str):
        self.producer.produce(
            topic=self.topic,
            key=key,
            value=value,
            callback=self.delivery_report
        )
        self.producer.flush()  # Wait for message to be sent
