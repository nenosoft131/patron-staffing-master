from message import Message


class SmsService(Message):
    
    def send(self, title: str, message: str):
        return f" {title} : {message} : SMS" 
