from django import forms
from  . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'published_at', 'author']