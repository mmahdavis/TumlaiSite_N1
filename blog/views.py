from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from blog.models import Post, PostConnectToCategory, Category, PostComment
from django.db.models import Q


def blog_details(request, pk):
    posts = Post.objects.get(id = pk)
    comments = PostComment.objects.filter(post_id = pk)
    return render(request, 'blog_details.html', {'posts': posts, 'comments': comments})


def blog_list(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    cap = Category.objects.filter(project__name__contains="Foo")
    return render(request,'tumlai_blog.html', {'posts': posts, 'category': category})
