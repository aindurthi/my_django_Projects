# -*- coding: utf-8 -*-
'''from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Testing fb</h1>")'''

from django.shortcuts import render

def index(request):
	return render(request, 'fbposter/index.html')
