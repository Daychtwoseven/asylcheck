import os

from twilio.rest import Client
from bs4 import BeautifulSoup
from datetime import date

from main.settings import BASE_DIR
from .models import *

def sms(to, message):
    authentication = Authentication.objects.filter(id=1).first()
    client = Client(authentication.twillio_sid, authentication.twillio_token)

    message = client.messages.create(
        to=to,
        from_="+15074364290",
        body=message)

    return True


def generate_html(data):
    if data:
        today = date.today()
        HTMLFile = open(os.path.join(BASE_DIR, f'base.html'), 'r', encoding='utf-8')
        index = HTMLFile.read()
        html = BeautifulSoup(index, 'html.parser').prettify().replace('DateHere', today.strftime("%B %d, %Y")).replace('FullName', data.name if data.name else '').replace('PassportID', data.passport_id if data.passport_id else '').replace('FNLOWER', data.name if data.name else '').replace('DateofBirth', data.passport_birthdate if data.passport_birthdate else '')
        return ComplaintDocs.objects.create(complaint=data, html_file=html)

