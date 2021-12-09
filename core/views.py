from typing import TextIO
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q



def home_page(request):
    post_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)

    tags = Tag.objects.annotate(t_count=Count('post')).order_by('-t_count')[:8]
    popular = Post.objects.order_by('-view_count')[:4]


    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'tags': tags,
        'popular': popular
    }

    return render(request, 'home.html', context)


def category(request, pk):
    pass

def article_page(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.annotate(t_count=Count('post')).order_by('-t_count')[:8]
    popular = Post.objects.order_by('-view_count')[:4]

    context = {
        'post': post,
        'tags': tags,
        'popular': popular,
    }
    return render(request, 'article.html', context)