# Generated by Django 4.0.5 on 2022-06-10 13:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('mainwebsite', '0011_rename_content_article_my_field_article_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Blog',
        ),
    ]
