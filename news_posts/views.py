from django.shortcuts import render, get_object_or_404, get_list_or_404
from collections import defaultdict

# Create your views here.

from .models import Post
from ImageUploader.models import Image


def news(request):
    template = 'news.html'
    try:
        post = Post.objects.latest('date')
    except Post.DoesNotExist:
        post = None
    try:
        images = Image.objects.filter(post=post)
    except Image.DoesNotExist:
        images = None
    context = {
        'post':post,
        'images':images,
    }
    return render(request, template, context)

def specific_post(request, post_slug):
    template = 'specific_news.html'
    post = get_object_or_404(Post, slug=post_slug)
    try:
        images = Image.objects.filter(post=post)
    except Image.DoesNotExist:
        images = None
    context = {
        'post':post,
        'images':images,
    }
    return render(request, template, context)


def archive(request):
    template = 'archive.html'
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    if posts:
        arc = []
        for post in posts:
            arc.append({'post': post,  'date':post.date})

    context = {
        'archive': arc,
    }
    return render(request, template, context)