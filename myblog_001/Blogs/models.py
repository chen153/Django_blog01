from django.db import models

# Create your models here.


class BlogsTest(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    address = models.CharField(max_length=200, verbose_name='Address')
    city = models.CharField(max_length=60, verbose_name='City')
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class BlogsList(models.Model):

    name = models.CharField(max_length=30, verbose_name='Name')
    author = models.CharField(max_length=50, verbose_name='Author')
    category = models.CharField(max_length=60, verbose_name='Category')
    blog_date = models.DateTimeField(verbose_name='Date')
    blog_content = models.TextField(verbose_name='Contents')
    blog_img = models.ImageField(verbose_name='Image', upload_to='blogs/')

