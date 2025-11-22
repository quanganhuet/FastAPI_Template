import redis
from functools import wraps
from app.core.redis import redis_client

# Example cache decorator

def redis_cache(key_prefix: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{key_prefix}:{args}:{kwargs}"
            cached = redis_client.get(key)
            if cached:
                return cached
            result = func(*args, **kwargs)
            redis_client.set(key, result)
            return result
        return wrapper
    return decorator
