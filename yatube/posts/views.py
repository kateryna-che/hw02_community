from django.shortcuts import get_object_or_404, render

from .models import Group, Post
from django.conf import settings


def index(request):
    posts = Post.objects.all()[:settings.POSTS_LIMIT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:settings.POSTS_LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
