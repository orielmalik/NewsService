import redis
from flask import Flask, jsonify
import json

import ValidationUtils


#REDIS service for  HOTTEST NEWS(1 hour and expired)
class RedisConnector:
    def __init__(self):
        self.redis_client = None
        self.connect()  # Connect to Redis on initialization

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
            self.connect()  # Reconnect if necessary

    def ping(self):
        try:
            return self.redis_client.ping()
        except:
            return False  # Handle potential exceptions

    def create_content(self, content):
        if content is not None:
            # Check if content exists before creating a new one
            existing_content = self.redis_client.get(content.id)
            if existing_content is None:
                self.redis_client.set(content.id, json.dumps(content.to_dict()),ex=3600)
                return jsonify({"message": "NEW CONTENT OBJECT CREATED", "content": self.redis_client.get(content.id)}, 200)
            else:
                return jsonify({"error": "Content with ID already exists"}), 400
        else:
            return jsonify({"error": "Invalid content object"}), 400  # Handle missing content

    def delete_content(self,id='all'):
        if id == 'all':
            for k in self.redis_client.keys:
                 self.redis_client.delete(k)
        elif id in self.redis_client.keys():
            self.redis_client.delete(id)
        else:
            return jsonify({"error": "not DELETE"}),400
        return jsonify({"message": "DELETE work"}),200

    def put_content(self,content):
        if not ValidationUtils.validate_email(content.email):
            return jsonify({"error","email"}),401
        if content.id   in self.redis_client.keys():
            self.redis_client.set(content.id, json.dumps(content.to_dict()))
        else:
            return jsonify({"error": "not updated"}),400


    def get_content(self,type='all'):
        if type == 'all':
            return self.redis_client.get(pattern='*').decode('utf-8')
        else:
            return self.redis_client.get(pattern=type).decode('utf-8')
