# Generated by Django 3.2.5 on 2021-12-07 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_alter_diary_diary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='diary_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 7, 16, 4, 34, 550548)),
        ),
    ]
