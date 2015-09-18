from django import forms
from .models import Post, Comment, Tool

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = (
				'title', 
				'text', 
				'image', 
				'duration',
				)

class CommentForm(forms.ModelForm):
	 class Meta:
	 	model = Comment
	 	fields = ('author', 'text',)


class ToolForm(forms.ModelForm):
	class Meta:
		model = Tool
		fields = ('tool_type',)