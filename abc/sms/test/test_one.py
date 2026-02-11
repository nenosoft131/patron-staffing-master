from service.email_service import EmailService
from service.sms_service import SmsService
from service.message_service import MessageService
from service.data import Data
import pytest


@pytest.fixture
def obj_email():
    return EmailService()

@pytest.fixture
def obj_sms():
    return SmsService()


def test_service(obj_email,obj_sms):
    
    data = Data(title="USMAN", message="Start")
    service = MessageService(obj_email)
    res = service.transmit(data)
    assert res == " USMAN : Start : Email"