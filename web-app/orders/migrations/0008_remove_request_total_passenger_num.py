# Generated by Django 2.1.5 on 2019-01-27 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_request_total_passenger_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='total_passenger_num',
        ),
    ]