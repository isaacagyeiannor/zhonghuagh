# Generated by Django 4.0.5 on 2022-06-11 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0014_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='PageTitle',
            new_name='locationSubText',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='SubText',
            new_name='pageTitle',
        ),
    ]
