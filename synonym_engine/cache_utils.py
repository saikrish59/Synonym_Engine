import redis
import json
import os
from dotenv import load_dotenv

load_dotenv()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0
)

def get_from_cache(key):
    data = redis_client.get(key)
    return json.loads(data) if data else None

def save_to_cache(key, data, ttl=3600):
    redis_client.setex(key, ttl, json.dumps(data))
