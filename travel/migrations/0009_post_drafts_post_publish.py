# Generated by Django 4.2.10 on 2024-02-16 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='drafts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2024, 2, 16, 21, 9, 58, 665643, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]