from unicodedata import category
from django import template
from blog.models import Category, Post, Comment

register = template.Library()


@register.inclusion_tag('blog/latest-post.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/category.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}        


@register.simple_tag(name="comments_count")
def comments_count(pid):
    return Comment.objects.filter(post=pid ,approved=True).count()