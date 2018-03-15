from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'login/[html file here]') #needs the html file name