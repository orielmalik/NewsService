import uuid
from ValidationUtils import *


class CONTENT():
    def __init__(self, id='', body='', author=None):
        self.id =str(uuid.uuid4())
        self.body = body
        if author is not None :
            self.author = author
            self.published = False
            self.timestamp = getTime()



    def to_dict(self):
        return {
            "id": self.id,
            "body": self.body
        }
