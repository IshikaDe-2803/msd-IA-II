# Generated by Django 4.2 on 2023-04-28 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_api', '0004_alter_newvideo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newvideo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]