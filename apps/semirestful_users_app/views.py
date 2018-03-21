# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import User

def index(request):
    users = User.objects.all()
    context = {
        "all_users" : users
    }
    return render(request, "semirestful_users_app/index.html", context)

def new(request):
    print('entered new')
    return render(request, "semirestful_users_app/new.html")


def create(request):
    print('entered create')
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    print(new_user.first_name)
    print(new_user.last_name)
    print(new_user.email)
    print(new_user.id)
    return redirect('/users')

def show(request, id):
    print('entered show')
    context = {
        "my_user" : User.objects.get(id=id)
    }
    return render(request, "semirestful_users_app/show.html", context)

def edit(request, id):
    context = {
        "my_user" : User.objects.get(id=id)
    }
    return render(request, "semirestful_users_app/edit.html", context)

def update(request):
    print('entered update!')
    my_user_id = request.POST['user_id']
    my_user_first_name = request.POST['first_name']
    my_user_last_name = request.POST['last_name']
    my_user_email = request.POST['email']
    b = User.objects.get(id=my_user_id)
    b.first_name = my_user_first_name
    b.last_name = my_user_last_name
    b.email = my_user_email
    b.save()
    print(my_user_id)
    return redirect('/users')

def delete(request, id):
    print('entered delete!')
    b = User.objects.get(id=id)
    b.delete()
    return redirect('/users')