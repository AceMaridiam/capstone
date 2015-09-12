from django.db import models
from django.utils import timezone
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

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