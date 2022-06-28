# Generated by Django 4.0.5 on 2022-06-28 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summaryTitle', models.CharField(max_length=200)),
                ('summaryNumber', models.CharField(max_length=200)),
                ('totalNumber', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
                ('titleTag', models.CharField(max_length=50)),
                ('pageTitle', models.CharField(max_length=50)),
                ('contactUs', tinymce.models.HTMLField()),
                ('locationHeading', models.CharField(max_length=50)),
                ('locationText', models.CharField(max_length=50)),
                ('locationSubText', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('mapUrl', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galleryTitle', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeAboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutUsTitle', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=20, null=True, upload_to='images/')),
                ('headingTag', models.CharField(max_length=200)),
                ('heading', models.CharField(max_length=200)),
                ('paragraph', models.CharField(max_length=200)),
                ('list1', models.CharField(max_length=200)),
                ('list2', models.CharField(max_length=200)),
                ('list3', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whyUsTitle', models.CharField(max_length=200)),
                ('image1', models.ImageField(max_length=20, null=True, upload_to='images/')),
                ('image2', models.ImageField(max_length=20, null=True, upload_to='images/')),
                ('headingTag', models.CharField(max_length=200)),
                ('heading1', models.CharField(max_length=200)),
                ('heading2', models.CharField(max_length=200)),
                ('heading3', models.CharField(max_length=200)),
                ('paragraph', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainAbout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=50)),
                ('titleTag', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MainBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=50)),
                ('titleTag', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MainGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MainServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteTitle', models.CharField(max_length=50)),
                ('serviceTitle', models.CharField(max_length=30, null=True)),
                ('serviceTag', models.CharField(max_length=30, null=True)),
                ('backgroundImage', models.ImageField(max_length=30, null=True, upload_to='')),
                ('titleTag', models.CharField(max_length=50)),
                ('pageTitle', models.CharField(max_length=50)),
                ('serviceHeading', models.CharField(max_length=50)),
                ('headingTag', models.CharField(max_length=50)),
                ('servicetext', tinymce.models.HTMLField()),
                ('ourExpertiseHeading', models.CharField(max_length=50)),
                ('expertiseImage', models.ImageField(max_length=30, null=True, upload_to='')),
                ('companyPDF', models.FileField(upload_to='')),
                ('list1', models.CharField(max_length=50)),
                ('list2', models.CharField(max_length=50)),
                ('list3', models.CharField(max_length=50)),
                ('list4', models.CharField(max_length=50)),
                ('telImage', models.ImageField(max_length=30, null=True, upload_to='')),
                ('tel', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceTitle', models.CharField(max_length=200)),
                ('serviceNumber', models.IntegerField()),
                ('image', models.ImageField(max_length=20, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rsnumber', models.CharField(max_length=200)),
                ('image', models.ImageField(max_length=20, null=True, upload_to='')),
                ('lighttext', models.CharField(max_length=200)),
                ('boldtext', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonialTitle', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('companyname', models.CharField(max_length=20)),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
                ('testimony', models.CharField(default='testimony nkoaa', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('my_field', tinymce.models.HTMLField()),
                ('image', models.ImageField(max_length=30, null=True, upload_to='')),
                ('category', models.CharField(default='uncategorized', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
