import uuid
from ValidationUtils import *
class CONTENT:
    def __init__(self, body='', author='NONE',id=None):
        self.id = id if id else str(uuid.uuid4())
        self.body = body
        self.createdTimeStamp = datetime.now()
        self.authorId =author

    def to_dict(self):
        return {
            "id": self.id,
            "body": self.body,
            "createdTimeStamp": self.createdTimeStamp,
            "authorId": self.authorId
        }
    def get_id(self):
        return self.id
    @staticmethod
    def from_dict(di):
        return CONTENT(
            id=di.get('id'),
            body=di.get('body', '')
        )
