# Generated by Django 4.1.7 on 2023-03-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_complaints_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
