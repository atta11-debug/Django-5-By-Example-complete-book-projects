from django import template
from blog.models import Post
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=3):
    latest_posts = Post.objects.order_by("-publish")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(num=3):
    return Post.objects.annotate(total_comments=Count("comments")).order_by(
        "-total_comments"
    )[:num]

@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))