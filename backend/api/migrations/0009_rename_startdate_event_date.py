# Generated by Django 4.2 on 2023-05-18 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_type_event_lan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='startDate',
            new_name='date',
        ),
    ]
