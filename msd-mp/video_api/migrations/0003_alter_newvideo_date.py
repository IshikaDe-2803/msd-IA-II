# Generated by Django 4.2 on 2023-04-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0002_alter_newvideo_date_alter_newvideo_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideo',
            name='date',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
