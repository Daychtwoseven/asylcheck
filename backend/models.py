from django.db import models
import uuid


class Complaints(models.Model):
    STEPS_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    verification_code = models.CharField(max_length=255, null=True)
    step = models.CharField(max_length=255, choices=STEPS_CHOICES, default='1')
    date_created = models.DateTimeField(auto_now_add=True)
    # Received Asylum Notice
    received = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    passport_name = models.CharField(max_length=255, null=True, blank=True)
    passport_date_issued = models.CharField(max_length=255, null=True, blank=True)
    passport_front = models.CharField(max_length=255, null=True, blank=True)
    passport_back = models.CharField(max_length=255, null=True, blank=True)
    passport_birthdate = models.CharField(max_length=255, null=True, blank=True)
    passport_id = models.CharField(max_length=255, null=True, blank=True)
    docs_url = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name} | Phone: {self.phone}'


class ComplaintsQueing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.ForeignKey(Complaints, models.RESTRICT)
    completed = models.BooleanField(default=False)


class ComplaintDocs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    complaint = models.ForeignKey(Complaints, models.RESTRICT)
    html_file = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)