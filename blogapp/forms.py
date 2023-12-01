from dataclasses import fields
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'slug', 'author', 'content', 
                  'post_image', 'category']
        

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'author', 'content', 
                  'post_image', 'category']
        