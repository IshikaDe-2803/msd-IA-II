# Generated by Django 4.2 on 2023-04-26 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0003_alter_newvideo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideo',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]