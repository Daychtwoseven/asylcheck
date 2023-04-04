from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('', index_page, name='backend-index-page'),
    path('step1/', step1_page, name='backend-step1-page'),
    path('step2/', step2_page, name='backend-step2-page'),
    path('step3/', step3_page, name='backend-step3-page'),
    path('step4/', step4_page, name='backend-step4-page'),
    path('docs/<slug:pk>/', docs_page, name='backend-docs-page'),
    path('confirm/<slug:pk>/', confirm_page, name='backend-confirm-page')
]
