from django.contrib import admin
from Blogs.models import BlogsTest, BlogsList
# Register your models here.


class BlogsTestAdmin(admin.ModelAdmin):
    # 在表中只显示('name', 'email')
    # fields = ('name', 'email')
    list_display = ('id', 'name', 'address', 'city', 'state_province', 'country', 'website')
    list_display_links = ('id', 'name')


class BlogsListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category', 'blog_date')
    list_display_links = ('id', 'name', 'category', 'author')


admin.site.register(BlogsTest, BlogsTestAdmin)
admin.site.register(BlogsList, BlogsListAdmin)
