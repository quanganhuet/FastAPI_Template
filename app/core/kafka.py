from kafka import KafkaProducer, KafkaConsumer
from app.core.config import settings
import json

producer = KafkaProducer(
    bootstrap_servers=[settings.kafka_broker],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_consumer(topic, group_id='fastapi-group'):
    return KafkaConsumer(
        topic,
        bootstrap_servers=[settings.kafka_broker],
        group_id=group_id,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )
