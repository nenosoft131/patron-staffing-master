from abc import ABC, abstractmethod

class Message(ABC):
    
    @abstractmethod
    def send(self, title:str , message:str):
        raise NotImplemented