# Generated by Django 3.1.1 on 2020-09-21 09:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_auto_20200920_1421'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdditionalArtistDetails',
            new_name='AdditionalArtistDetail',
        ),
    ]