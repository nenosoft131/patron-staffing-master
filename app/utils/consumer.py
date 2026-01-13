
import yaml
import json
import threading
from kafka import KafkaConsumer

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def start_consumer():
    config = load_config()["kafka"]

    consumer = KafkaConsumer(
        config["topic"],
        bootstrap_servers=config["bootstrap_servers"],
        group_id=config["group_id"],
        auto_offset_reset=config["auto_offset_reset"],
        enable_auto_commit=config["enable_auto_commit"],
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )
    for message in consumer:
        process_message(message.value)

def process_message(message):
    print(f"Consumed message: {message}")

def run_consumer_in_thread():
    thread = threading.Thread(target=start_consumer, daemon=True)
    thread.start()
