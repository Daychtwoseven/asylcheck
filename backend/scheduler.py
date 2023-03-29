from apscheduler.schedulers.background import BackgroundScheduler
from . utils import sms, generate_html
from . models import *
import time

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_all, 'interval', minutes=2)
    scheduler.start()


def run_all():
    queing = ComplaintsQueing.objects.filter(completed=False).all()
    print(queing)
    for row in queing:
        complaint = row.complaint
        phone = complaint.phone
        docs = generate_html(complaint)
        sms(phone, f"Your document has been created, see here: localhost:8000/docs/{str(docs.id)}/")
        """
        sms(phone, f"Thank you for your document, Your document is on hold and will be processed shortly.")
        time.sleep(20)
        sms(phone, f"Your document is currently being created and will be sent to you shortly.")
        time.sleep(20)
        sms(phone, f"Your document has been created, see here: localhost:8000/docs/{str(docs.id)}/")
        sms(phone, f"Your document has been created and will now be assigned to a lawyer for legal review. "
                   f"You can see the document here: localhost:8000/docs/{str(docs.id)}/ ")
        time.sleep(20)
        sms(phone, f"Your responsible lawyer is Mag. Jodlbauer from the law firm HBA Rechtsanwälte. "
                   f"He will review and submit the document.")
        time.sleep(20)
        #sms(phone, 'sample message')
        sms(phone, 'Your default complaint was examined submitted to the BFA. You should now receive your '
                   'notification within 3 months.')
        """
        row.completed = True
        row.save()
