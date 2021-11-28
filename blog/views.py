from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from blog.models import Post, PostConnectToCategory, Category, PostComment
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_details(request, pk):
    posts = Post.objects.get(id = pk)
    comments = PostComment.objects.filter(post_id = pk)
    return render(request, 'blog_details.html', {'posts': posts, 'comments': comments})


def blog_list(request, tag_slug=None):
    posts = Post.objects.all()
    category = Category.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'tumlai_blog.html', {'posts': posts, 'category': category, 'page': page})
