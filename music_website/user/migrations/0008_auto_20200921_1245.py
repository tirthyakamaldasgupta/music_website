# Generated by Django 3.1.1 on 2020-09-21 12:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0007_auto_20200921_0944'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdditionalStudentDetail',
            new_name='AdditionalListenerDetail',
        ),
    ]