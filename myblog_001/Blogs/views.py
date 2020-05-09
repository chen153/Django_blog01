#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from Blogs.models import BlogsTest, BlogsList
import json


def blogs(request):
    # context = {"data1": Test.objects.order_by("-time")[0].temp1,
    #            "data2": Test.objects.order_by("-time")[0].temp2}
    data = BlogsList.objects.all()
    # print(data[0].name)
    context = {}
    context.update({
        'msg': 'Hello World!',
        'data': data,
    })
    return render(request, 'blogs.html', context)

def blogs_list(request, blog_id):
    data = BlogsList.objects.all()
    data1 = data.filter(id=int(blog_id))
    context = {}
    context.update({
        'msg': 'Hello World!',
        'data': data1,
    })
    print(data1[0].id)
    return render(request, 'blogs_content.html', context)

def response_success(message, data=None, data_list=[]):
    return HttpResponse(json.dumps({
        'code': 2000,#code由前后端配合指定
        'message': message,#提示信息
        'data': data,#返回单个对象
        'dataList': data_list#返回对象数组
    }), 'application/json')

def files_ajax(request):
    # 提交文件从,request.FILES中取,提交的数据,从request.POST中取
    # name=request.POST.get('name')
    # print(name)
    # dic_files = request.FILES
    # myfile = dic_files.get('myfile')
    # with open(myfile.name, 'wb') as f:
    #     # 循环上传过来的文件
    #     for line in myfile:
    #         # 往空文件中写
    #         f.write(line)
    v = {
        'name': 'charlie',
        'age': 18
    }
    return HttpResponse(json.dumps(v))

