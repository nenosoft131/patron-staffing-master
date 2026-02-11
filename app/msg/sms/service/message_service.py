from message import Message
from data import Data


class MessageService():
    
    def __init__(self, obj:Message):
        self._obj = obj
        
    def transmit(self, data :Data):
        return self._obj.send(title=data.title, message=data.message)