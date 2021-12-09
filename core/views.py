from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q



def home_page(request):
    categories = Category.objects.filter(for_navbar=True)[:8]
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
        'popular': popular,
        'categories': categories
    }

    return render(request, 'home.html', context)


def by_category(request, slug):
    categories = Category.objects.filter(for_navbar=True)[:8]
    category = get_object_or_404(Category, slug=slug)
    post_list = category.posts.all()
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
        'popular': popular,
        'categories': categories

    }

    return render(request, 'home.html', context)


def by_tag(request, slug):
    categories = Category.objects.filter(for_navbar=True)[:8]
    tag = get_object_or_404(Tag, slug=slug)
    post_list = tag.post_set.all()
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
        'popular': popular,
        'categories': categories

    }

    return render(request, 'home.html', context)



def article_page(request, slug):
    categories = Category.objects.filter(for_navbar=True)[:8]
    post = get_object_or_404(Post, slug=slug)
    tags = Tag.objects.annotate(t_count=Count('post')).order_by('-t_count')[:8]
    popular = Post.objects.order_by('-view_count')[:4]
    related = Post.objects.filter(

    )

    context = {
        'post': post,
        'tags': tags,
        'popular': popular,
        'categories': categories

    }
    return render(request, 'article.html', context)


def search(request):
    categories = Category.objects.filter(for_navbar=True)[:8]
    q = request.GET.get('q')
    post_list = Post.objects.filter(
        Q(title__icontains=q) | Q(category__name__icontains=q) | Q(tags__name__icontains=q) | Q(description__icontains=q)
    ).distinct()
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
        'popular': popular,
        'categories': categories

    }

    return render(request, 'home.html', context)