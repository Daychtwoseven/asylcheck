from twilio.rest import Client
from bs4 import BeautifulSoup
from datetime import date
from .models import *

# Your Account SID from twilio.com/console
account_sid = "ACd6201ff228841b9af0cc26a54d9088ea"
# Your Auth Token from twilio.com/console
auth_token = "7a964b9c833fadad6e0f6e86f3fabe03"


def sms(to, message):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=f"+{to}",
        from_="+15074364290",
        body=message)

    return True


def generate_html(data):
    if data:
        today = date.today()
        HTMLFile = open('base.html', 'r', encoding='utf-8')
        index = HTMLFile.read()
        html = BeautifulSoup(index, 'html.parser').prettify().replace('DateHere', today.strftime("%B %d, %Y")).replace('FullName', data.name if data.name else '').replace('PassportID', data.passport_id if data.passport_id else '').replace('FullNameLower', data.name if data.name else '').replace('DateofBirth', data.passport_birthdate if data.passport_birthdate else '')
        return ComplaintDocs.objects.create(complaint=data, html_file=html)
