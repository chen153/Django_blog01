"""myblog_001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog_001.views import index
from Blogs.views import blogs, blogs_list, files_ajax
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理路由
    path('', index, name='Home'),  # path设置为空，表示打开首页
    path('blogs/', blogs, name='Blogs'),
    path('blogs/ajax/', files_ajax, name='Ajax'),
    path('blogs/<int:blog_id>', blogs_list, name='blogPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 后台管理标题设置
admin.site.site_header = 'MyBlogs-后台管理'
admin.site.site_title = 'My-Blogs'