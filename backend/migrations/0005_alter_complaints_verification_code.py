# Generated by Django 4.1.7 on 2023-03-21 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_complaints_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='verification_code',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
