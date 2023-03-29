import base64

from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from . models import *
from . utils import *
import random
import requests


def index_page(request):
    try:
        context = {
            'data': None
        }
        if request.method == "POST":
            name = request.POST.get('name')
            phone = request.POST.get('phone')

            complaint = Complaints.objects.filter(phone=phone).first()
            if not complaint:
                context['data'] = Complaints.objects.create(name=name, phone=phone)
                return render(request, 'backend/step1.html', context)
            else:
                print(complaint.step)
                context['data'] = complaint
                return render(request, f'backend/step{complaint.step}.html', context)

        return render(request, 'backend/index.html')
    except Exception as e:
        print(e)


def step1_page(request):
    try:
        if request.method == "POST":
            context = {
                'data': None
            }
            received = True if request.POST.get('value') == "True" else False
            complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
            complaint.received = received
            complaint.step = "2"
            complaint.save()
            context['data'] = complaint
            print(context['data'])
            return render(request, 'backend/step2.html', context)
    except Exception as e:
        print(e)


def step2_page(request):
    try:
        if request.method == "POST":
            context = {
                'data': None
            }
            code = random.randint(100000, 999999)
            send_sms = sms(request.POST.get('phone'), f"Your verification code is {code} asylcheck.com")
            complaint = Complaints.objects.filter(id=request.POST.get('pk')).first()
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

                    img_url_front = f"https://asylcheck2023.pythonanywhere.com/attachments/Specimen_Personal_Information_Page_South_Korean_Passport.jpg"
                    img_url_back = f"https://asylcheck2023.pythonanywhere.com/attachments/Specimen_Personal_Information_Page_South_Korean_Passport.jpg"
                    req_front = requests.get('https://api.pixlab.io/docscan', params={
                        'img': img_url_front,
                        'type': 'passport',
                        'key': '41285298aa12076448bf98ac16a5f1fd',
                        'orientation': True
                    })
                    req_back = requests.get('https://api.pixlab.io/docscan', params={
                        'img': img_url_back,
                        'type': 'passport',
                        'key': '41285298aa12076448bf98ac16a5f1fd',
                        'orientation': True
                    })

                    reply_front = req_front.json()
                    reply_back = req_back.json()
                    if reply_front['status'] != 200 or reply_back['status'] != 200:
                        print(reply_front['error'])
                        print(reply_back['error'])
                    else:
                        print(reply_front)
                        print(reply_back)
                        name = reply_front['fields']['fullName']
                        date_issued = reply_back['fields']['dateOfIssued'] if 'dateOfIssued' in reply_back['fields'] else ''
                        complaint.passport_name = name
                        complaint.passport_date_issued = date_issued
                        complaint.passport_front = front_name
                        complaint.passport_back = back_name
                        complaint.passport_birthdate = reply_front['fields']['dateOfBirth']
                        complaint.save()
                        print(complaint)
                        docs = generate_html(complaint)
                        url = f"https://asylcheck2023.pythonanywhere.com/docs/{str(docs.id)}/"
                        complaint.docs_url = url
                        complaint.save()
                        sms(complaint.phone, f"Your document has been created and is ready for review, see here: {url}")
                        #queing = ComplaintsQueing.objects.create(complaint=complaint)
                        return render(request, 'backend/final.html')
                    return JsonResponse(reply_front)

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
        print(e)