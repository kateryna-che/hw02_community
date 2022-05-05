from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    POSTS_LIMIT = 10
    posts = Post.objects.all()[:POSTS_LIMIT]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    POSTS_LIMIT = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:POSTS_LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
