from django.shortcuts import render
from .forms import PostForm
from .models import Input 
from django.Http import HttpResponseRedirect
# Create your views here.

def index(request):
	return render(request, 'input/scheduler.htm')

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('input/scheduler.html')
	else:
		form = PostForm()
	return render(request, 'scheduler.htm', {'form':form})