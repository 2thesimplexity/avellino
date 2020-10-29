from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Post
        fields= "__all__"
       

        


'''remove the stupid colon followed by label that's automatically come with Django forms'''
'''It worked yesterday, why doesn't it work today???'''

def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(PostForm, self).__init__(*args, **kwargs)