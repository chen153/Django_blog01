#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    context = {
        'index': 'Hello World!'
    }
    return render(request, 'index.html', context)