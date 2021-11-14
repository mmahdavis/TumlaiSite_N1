from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

def home_page(request):
    return render(request, 'home-2.html',{})