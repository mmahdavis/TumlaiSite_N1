from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from blog.models import Post, PostConnectToCategory, Category
from django.db.models import Q


def home_page(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def about_us(request):
    return render(request, 'about_us.html', {})


def not_found(request):
    return render(request, '404.html', {})
