# Generated by Django 4.0.5 on 2022-06-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0004_testimonial_testimony_alter_testimonial_companyname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimony',
            field=models.CharField(default='testimony nkoaa', max_length=200),
        ),
    ]
