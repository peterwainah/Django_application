# Generated by Django 2.2.7 on 2020-01-14 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0006_scholarshipapplication_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarshipapplication',
            name='email',
        ),
    ]
