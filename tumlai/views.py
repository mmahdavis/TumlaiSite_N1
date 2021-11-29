from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from blog.models import Post, Category
from django.db.models import Q
from django.http import HttpResponseNotFound

def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about_us(request):
    return render(request, 'about_us.html', {})


def not_found(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
