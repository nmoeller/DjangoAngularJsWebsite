# Generated by Django 2.0.2 on 2018-03-11 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='ansprechpartner',
        ),
        migrations.RemoveField(
            model_name='player',
            name='trainer',
        ),
    ]
