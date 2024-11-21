import redis
from flask import Flask, jsonify
import json

class RedisConnector:
    def __init__(self):
        self.redis_client = None
        self.connect()

    def connect(self):
        try:
            self.redis_client = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
            self.redis_client.ping()
            print("Connected to Redis")
        except Exception as e:
            print(f"Failed to connect to Redis: {e}")
            self.redis_client = None

    def ensure_connection(self):
        if self.redis_client is None or not self.ping():
            print("Reconnecting to Redis...")
            self.connect()

    def create_content(self, content):
        if self.redis_client.get(content.id) is None:
            self.redis_client.set(content.id, json.dumps(content.to_dict()))
            stored_content = self.redis_client.get(content.id)
            return jsonify(json.loads(stored_content))  # המרה מ-bytes ל-dict

        else:
            # מחזיר שגיאה אם המפתח כבר קיים
            return jsonify({"error": "exists id"}), 404
    def read_key(self, key):
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
        try:
            return self.redis_client.ping()
        except:
            return False
