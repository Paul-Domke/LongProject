from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'division/[html file here]') #needs the html file name that is 
	#stored in the templates directory
	