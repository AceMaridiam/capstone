from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['author']
		# fields = (
		# 		'title', 
		# 		'text', 
		# 		'image', 
		# 		'duration',
		# 		)

class CommentForm(forms.ModelForm):
	 class Meta:
	 	model = Comment
	 	fields = ('author', 'text',)
