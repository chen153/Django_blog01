#### 后台管理UI美化
pip3 install simpleui
#### 在setting.py中的INSTALLED_APPS的第一行添加
'simpleui'
#### 在urls.py 中添加以下代码
admin.site.site_header = 'MyBlogs-后台管理'
admin.site.site_title = 'My-Blogs'