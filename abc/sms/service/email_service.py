from message import Message

class EmailService(Message):
    def send(self, title: str, message: str):
        return f" {title} : {message} : Email" 
