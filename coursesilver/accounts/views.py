<<<<<<< HEAD:djangosched/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import login, logout
from accounts.forms import *

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('courses:list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('home:home-page')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/')
=======
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from accounts.forms import *

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('courses:list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('home:home-page')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('/')
>>>>>>> 02c780f1ac80b97570b219f73329027a23ae8c0a:coursesilver/accounts/views.py
