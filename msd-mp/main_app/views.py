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
    if request.method =='GET' and 'search_query' in request.GET:
        query = request.GET.get('search_query')
        # videos = NewVideo.objects.filter(Q(title__icontains=query))
        videos = requests.get('http://localhost:8000/api/videoapi/' + 'search/' + query).json()
    else:
        videos = requests.get('http://localhost:8000/api/videoapi/').json()
    return render(request, 'homepage.html', {'videos':videos})

def trending(request):
    videos = requests.get('http://127.0.0.1:8000/api/videoapi/trending').json()
    return render(request, 'trending.html', {'trending':videos})

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
        # make the API request
        response = requests.post('http://127.0.0.1:8000/api/videoapi/', data=data, files=files)
        if response.status_code == 201:
            return redirect('homepage')
    return render(request, 'upload.html', {})


@login_required
def logout(request):
    auth_logout(request)
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

def videoview(request, videoID):
    video = requests.get('http://localhost:8000/api/videoapi/' + str(videoID)).json()
    comments = requests.get('http://localhost:8000/api/commentapi/videos/' + str(videoID) + '/comments/').json()
    count = len(comments)
    video['visits'] = video['visits'] + 1
    if request.method == "POST":
        if 'Addcomment' in request.POST:
            comment_text = request.POST['Addcomment']
            data = {
                "user": request.user.pk,
                "username": request.user.username,
                "comment_text": comment_text,
            }
            requests.post('http://localhost:8000/api/commentapi/videos/' + str(videoID) + '/comments/', data=data)
        elif 'Like' in request.POST:
            video['likes'] = video['likes'] + 1
        elif 'Dislike' in request.POST:
            video['dislikes'] = video['dislikes'] + 1
        requests.patch('http://localhost:8000/api/videoapi/' + str(videoID), data=video)
        return redirect('ViewVideo', videoID=videoID)
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'videoView.html', {'video':video, 'comments':comments, 'count':count, 'num_visits': num_visits})