# Generated by Django 4.2 on 2023-05-27 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0012_alter_event_user_alter_locationcomment_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='event',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
