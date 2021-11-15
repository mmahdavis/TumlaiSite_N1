from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

def home_page(request):
    return render(request, 'index.html',{})

def contact_us (request):
    return render(request,'contact_us.html',{})

def about_us(request):
    return render(request, 'about_us.html',{})

def not_found(request):
    return render(request, '404.html',{})

def blog_details(request):
    return render(request,'blog_details.html',{})

def blog_list(request):
    return render(request,'tumlai_blog.html',{})