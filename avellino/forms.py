from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Post
        fields= "__all__"




