# Generated by Django 3.1.2 on 2020-11-22 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 8, 2, 51, 381431)),
        ),
    ]
