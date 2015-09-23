from django import template
from blog.models import Post

register = template.Library()
@register.simple_tag
def draft():
	posts = Post.objects.filter(published=False).order_by('created_date')
	num = len(posts)
	return num