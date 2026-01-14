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
