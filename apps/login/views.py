# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect ('/')
    request.session['user_id'] = result.id
    return redirect('/success')

def success(request):
    return render(request, 'login/success.html')

def login_view(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/home')

def home(request):
        return render(request, 'login/home.html')
