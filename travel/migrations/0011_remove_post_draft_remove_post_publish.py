# Generated by Django 4.2.10 on 2024-02-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_rename_drafts_post_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
