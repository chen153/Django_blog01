# Generated by Django 3.0.6 on 2020-05-08 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_blogslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogslist',
            name='blog_img',
            field=models.ImageField(default=None, upload_to='', verbose_name='Image'),
        ),
    ]
