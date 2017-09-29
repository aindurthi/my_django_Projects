# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Category,Page
from .forms import CategoryForm

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)

'''def detail(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('name')
    context_dict = {'categories': category_list}
    return render_to_response('rango/index.html', context_dict, context)'''

def detail(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('name')
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def details(request,cat_id):
    cat = get_object_or_404(Category, pk=cat_id)
    return render(request,'rango/details.html',{'cat': cat})

def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render_to_response('rango/category.html', context_dict, context)


def add_category(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    return render_to_response('rango/add_category.html', {'form': form}, context)




