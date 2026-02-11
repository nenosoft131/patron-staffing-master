from sms_service import SmsService
from email_service import EmailService
from message_service import MessageService
import logging
from data import Data

logger =  logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    logger.debug("hhhh")
    t = int(input())
    print(type(t))
    data = Data(title=t, message="Start")
    try:
        sms = SmsService()
        email = EmailService()
        service = MessageService(sms)
        
        res = service.transmit(data)
        print(res)
    except Exception as e:
        logger.exception("ERROR")

if __name__ == '__main__':
    main()