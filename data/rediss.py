import redis

class RedisConnector:
    def __init__(self):
        self.redis_client = None
        self.connect()  # להתחבר בעת יצירת המחלקה

    def connect(self):
        try:
            self.redis_client = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
            # בדיקה אם החיבור עובד
            self.redis_client.ping()
            print("Connected to Redis")
        except Exception as e:
            print(f"Failed to connect to Redis: {e}")
            self.redis_client = None

    def ensure_connection(self):
        """בדוק אם החיבור פעיל, ואם לא - התחבר מחדש."""
        if self.redis_client is None or not self.ping():
            print("Reconnecting to Redis...")
            self.connect()

    def create_or_update_key(self, key, value):
        self.ensure_connection()
        try:
            self.redis_client.set(key, value)
            return f"Key '{key}' created/updated successfully."
        except Exception as e:
            return f"Failed to create/update key '{key}': {e}"

    def read_key(self, key):
        self.ensure_connection()
        try:
            value = self.redis_client.get(key)
            if value is None:
                return f"Key '{key}' does not exist."
            return value
        except Exception as e:
            return f"Failed to read key '{key}': {e}"

    def delete_key(self, key):
        self.ensure_connection()
        try:
            result = self.redis_client.delete(key)
            if result == 0:
                return f"Key '{key}' does not exist or already deleted."
            return f"Key '{key}' deleted successfully."
        except Exception as e:
            return f"Failed to delete key '{key}': {e}"

    def get_keys(self, pattern="*"):
        self.ensure_connection()
        try:
            keys = self.redis_client.keys(pattern)
            if not keys:
                return "No keys found."
            return keys
        except Exception as e:
            return f"Failed to retrieve keys: {e}"

    def ping(self):
        """בדוק אם החיבור ל-Redis פעיל."""
        try:
            return self.redis_client.ping()
        except:
            return False
