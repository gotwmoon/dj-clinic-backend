from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)

    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])

    context = {'posts':posts}
    return render(request, 'blog/blog-sidebar.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)
