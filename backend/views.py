from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from rosetta.translate_utils import translate
from .utils import *
import random
import requests
import json
import os


def index_page(request):
    try:
        context = {
            'data': None,
        }
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            prefix = request.POST.get('prefix')

            complaint = Complaints.objects.filter(phone=phone).first()
            if not complaint:
                context['data'] = Complaints.objects.create(name=name, phone=f"{prefix}{phone}")
                return render(request, 'backend/step1.html', context)
            else:
                context['data'] = complaint
                return render(request, f'backend/step{complaint.step}.html', context)

        return render(request, 'frontend/base/body.html')
    except Exception as e:
        print(e)


def step1_page(request):
    try:
        if request.method == "POST":
            context = {
                'data': None
            }
            received = True if request.POST.get('value') == "True" else False
            if not received:
                complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
                code = random.randint(100000, 999999)
                #send_sms = sms(complaint.phone, f"Your verification code is {code} asylcheck24")
                send_sms = True
                if send_sms and complaint:
                    complaint.received = received
                    complaint.verification_code = '1234'
                    #complaint.verification_code = code
                    complaint.step = '3'
                    complaint.save()
                    context['data'] = complaint
                    return render(request, 'backend/step3.html', context)
                else:
                    context[
                        'message'] = "We're sorry. Unfortunately we cannot process your case"
                    return render(request, 'backend/step5.html', context)
            else:
                context[
                    'message'] = "We're sorry. Unfortunately we cannot process your case"
                return render(request, 'backend/step5.html', context)
    except Exception as e:
        print(e)


def step2_page(request):
    try:
        if request.method == "POST":
            context = {
                'data': None
            }
            code = random.randint(100000, 999999)
            #send_sms = sms(request.POST.get('phone'), f"Your verification code is {code} asylcheck.com")
            complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
            send_sms = True
            if send_sms and complaint:
                complaint.verification_code = code
                complaint.step = '3'
                complaint.phone = request.POST.get('phone')
                complaint.save()
                context['data'] = complaint
                return render(request, 'backend/step3.html', context)
    except Exception as e:
        print(e)


def step3_page(request):
    try:
        if request.method == "POST":
            context = {
                'data': None
            }
            complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
            if complaint:
                if complaint.verification_code == request.POST.get('code'):
                    complaint.verified = True
                    complaint.step = '4'
                    complaint.save()
                    context['data'] = complaint
                    return render(request, 'backend/step4.html', context)
                return JsonResponse({'statusMsg': 'Invalid Code.'})
            return JsonResponse({'statusMsg': 'Invalid Access.'})
    except Exception as e:
        print(e)


def step4_page(request):
    try:
        context = {
            'data': None,
            'message': None
        }
        if request.method == "POST":
            complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
            if complaint:
                passport_front = [
                    {'passport_front': row}
                    for row in request.FILES.getlist('passport_front')
                ]

                passport_back = [
                    {'passport_back': row}
                    for row in request.FILES.getlist('passport_back')
                ]
                for front, back in zip(passport_front, passport_back):
                    fs = FileSystemStorage()
                    front_name = fs.save(front['passport_front'], front['passport_front'])
                    back_name = fs.save(back['passport_back'], back['passport_back'])

                    authentication = Authentication.objects.filter(id=1).first()
                    license_code = authentication.ocr_license_code
                    username = authentication.username

                    img_url_front = os.path.join(BASE_DIR, f'attachments/{front_name}')
                    img_url_back = os.path.join(BASE_DIR, f'attachments/{back_name}')
                    with open(img_url_front, 'rb') as front_image:
                        front_data = front_image.read()

                    with open(img_url_back, 'rb') as back_image:
                        back_data = back_image.read()
                    url = 'http://www.ocrwebservice.com/restservices/processDocument?gettext=true&newline=1'

                    front_request = requests.post(url, data=front_data, auth=(username, license_code))
                    back_request = requests.post(url, data=back_data, auth=(username, license_code))

                    if front_request.status_code == 200 and back_request.status_code == 200:
                        front_result = json.loads(front_request.content)
                        back_result = json.loads(back_request.content)

                        front_text = front_result['OCRText'][0][0].split('\n')
                        back_text = back_result['OCRText'][0][0].split('\n')

                        name = ''
                        passport_id = ''
                        birthdate = ''
                        date_issued = ''

                        for i in range(0, len(front_text)):
                            if front_text[i] == 'Name ':
                                name = ' '.join(front_text[i+1:i+3])
                            elif front_text[i] == 'Geburtsdatum ':
                                birthdate = front_text[i+1].replace(' ', '').replace('pm', '').replace('.', '-')
                            elif 'Karten Nr.' in front_text[i]:
                                passport_id = front_text[i].replace('Karten', '').replace('Nr.', '').replace(' ', '')

                        for i in range(0, len(back_text)):
                            if back_text[i] == 'Fremdenwesen and Asyl ':
                                date_issued = back_text[i+1].replace(' ', '').replace('.', '-')

                        complaint.passport_name = name
                        complaint.passport_date_issued = date_issued
                        complaint.passport_front = f"https://asylcheck2023.pythonanywhere.com/attachments/{front_name}/"
                        complaint.passport_back = f"https://asylcheck2023.pythonanywhere.com/attachments/{back_name}/"
                        complaint.passport_birthdate = birthdate
                        complaint.passport_id = passport_id
                        complaint.save()
                        docs = generate_html(complaint)
                        url = f"https://asylcheck2023.pythonanywhere.com/docs/{str(docs.id)}/"
                        complaint.docs_url = url
                        complaint.step = '5'
                        complaint.save()
                        # Send to complainant
                        #sms(complaint.phone, f"Your document has been created and is ready for review, see here: {url}")

                        # Send to lawyer
                        #sms('+4369919268828', f"Confirmation link for complainant {complaint.name}: https://asylcheck2023.pythonanywhere.com/confirm/{complaint.id}/")
                        context['message'] = 'Thanks for your Data! We will work on it shortly!'
                        return render(request, 'backend/step5.html', context)
                    else:
                        return JsonResponse({'statusMsg': 'Invalid File.'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'statusMsg': str(e)}, status=404)


def docs_page(request, pk):
    try:
        context = {
            'data': ComplaintDocs.objects.get(id=pk)
        }
        return render(request, 'frontend/base/docs.html', context)
    except Exception as e:
        return HttpResponse(status=404)


def confirm_page(request, pk):
    try:
        context = {
            'data': None
        }
        complaint = Complaints.objects.get(id=pk, confirm=False)
        print(complaint)
        if request.method == "POST":
            sms(complaint.phone,
                f"Your default complaint was examined by Mag. Jodlbauer and submitted to the BFA. You should now receive your notification within 3 months.")
            complaint.confirm = True
            complaint.save()
            context['message'] = f'You have successfully confirmed complainant'
            return render(request, 'backend/step5.html', context)
        else:
            context['data'] = complaint
            return render(request, 'backend/confirmation.html', context)
    except Exception as e:
        return HttpResponse(status=404)