# Generated by Django 2.0 on 2018-03-21 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20180321_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='webttFileName',
            new_name='webtt',
        ),
    ]
