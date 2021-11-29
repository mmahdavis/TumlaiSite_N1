from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from blog.models import Post, Category, PostComment
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import PostComment
from .forms import *


def blog_details(request, pk):
    posts = Post.objects.get(id=pk)
    comments = PostComment.objects.filter(post_id=pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            if name != None and email != None and title != None and message != None :
                message_content = PostComment(post_id=posts, user_name=name, email=email, title=title, content_text=message)
                message_content.save()
                messages.success(request, 'پیام شما با موفقیت ثبت شد')
                return redirect('/blog/%s/' % (pk))
            else:
                messages.warning(request, 'لطفا تمام فیلد ها را با اطلاعات صحیح تکمیل کنید')
                return redirect('/blog/%s/' % (pk))
        else:
            messages.error(request, 'خطا در ارتباط با سرور')
            return redirect('/blog/%s/' % (pk))

    return render(request, 'blog_details.html', {'posts': posts, 'comments': comments, 'forms': form})


def blog_list(request):
    recent_post = Post.objects.all()
    category = Category.objects.all()
    form = SearchForm(request.POST or None)
    posts = []
    if request.method == 'POST':
        if form.is_valid():
            search = form.cleaned_data.get('search')
            posts = Post.objects.filter(title__icontains=search).distinct()

    else:
        posts = Post.objects.all()

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
    context = {
        'page': page,
        'posts': posts,
        'forms': form,
        'recent_post': recent_post,
        'category': category
        }
    return render(request, 'tumlai_blog.html', context)
