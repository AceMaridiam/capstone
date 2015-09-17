from django.db import models
from django.utils import timezone
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

import urllib, hashlib
from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash

# Create your models here.

def generate_filename(instance, filename):
	ext = filename.split('.')[-1]
	return 'images/' + str(int(time())) + '.' + ext

class Post(models.Model):
	author         = models.ForeignKey('auth.User')
	title          = models.CharField(max_length=255)
	text           = models.TextField()
	created_date   = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	image          = models.ImageField(upload_to="images/", blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


@receiver(post_delete, sender=Post)
def image_post_delete_handler(sender, **kwargs):
	Post = kwargs['instance']
	storage, path = Post.image.storage, Post.image.path
	storage.delete(path)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.text

# Gravatar
# Set your variables here
email = "someone@somewhere.com"
default = "http://www.example.com/default.jpg"
size = 300
 
# construct the url
gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({'d':default, 's':str(size)})


