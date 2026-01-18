from fastapi import APIRouter
from pydantic import BaseModel
from producer import KafkaProducer

router = APIRouter()

# Kafka config
KAFKA_BROKER = "localhost:9092"
KAFKA_TOPIC = "test_topic"

kafka_producer = KafkaProducer(KAFKA_BROKER, KAFKA_TOPIC)

# Request body model
class Message(BaseModel):
    key: str
    value: str

# POST endpoint
@router.post("/send/")
async def send_message(message: Message):
    kafka_producer.send_message(message.key, message.value)
    return {"status": "Message sent", "key": message.key, "value": message.value}




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
        self.producer.flush()  # Wait for message to be s