from django import template

register = template.Library()


@register.filter
def only_comments_filter(comments):
    return comments.filter(active=True)


@register.filter
def count_only_comments_filter(comments):
    return comments.filter(active=True).count()
