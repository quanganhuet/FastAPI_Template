from app.core.kafka import producer
from app.events.topics import USER_CREATED

def send_user_created_event(data: dict):
    producer.send(USER_CREATED, data)
    producer.flush()
