# Generated by Django 4.1.7 on 2023-03-28 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_complaints_passport_back_complaints_passport_front'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=255)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.complaints')),
            ],
        ),
        migrations.CreateModel(
            name='MyDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_file', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='backend.complaints')),
            ],
        ),
    ]
