from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
import requests 
from .forms import UserRegistrationForm
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from datetime import date
import requests
# Create your views here.

def homepage(request):
    videos = requests.get('http://localhost:8000/api/videoapi/').json()
    print(videos)
    return render(request, 'homepage.html', {'videos':videos})

def trending(request):
    videos = requests.get('http://127.0.0.1:8000/api/videoapi/trending').json()
    print(videos)
    return render(request, 'trending.html', {'trending':videos})

def search(request):
    pass

def upload(request):
    if request.method == "POST":
        data = {
            'user': request.user.id,
            'username': request.user.username,
            'title': request.POST.get('title'),
            'description': request.POST.get('desc'),
        }
        files = {
            'thumbnail': request.FILES.get('thumbnail'),
            'video': request.FILES.get('video'),
        }
        print(data)
        print(files['thumbnail'])
        # make the API request
        response = requests.post('http://127.0.0.1:8000/api/videoapi/', data=data, files=files)
        if response.status_code == 201:
            return redirect('homepage')
    return render(request, 'upload.html', {})


@login_required
def logout(request):
    # auth_logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("homepage")

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"form": form}
    return render(request, "login.html", context)

def videoview(request):
    # SENJU ADD - create an api for comments and access comments by consuming that api
    # To create an api, create a new app called commentsapi or give some name
    # Follow the steps by referring the links or you can check the videoapi folder as well
    # You need to first add comments ka model in model.py. 
    # Add that model in admin.py
    # Create a serializer
    # Then create your views and add URLs as per need.
    # I think just a put/get request is more than enough, cause we are not providing functionality for delete and update.
    pass