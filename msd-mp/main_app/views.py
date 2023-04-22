from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import requests 
# Create your views here.


def get_books(request):
    url = 'http://localhost:8000/api/users/' 
    r = requests.get(url)
    books = r.json()
    books_list = {'books':books['results']}
    s = "abc"
    return HttpResponse("<h1>Page was found {} </h1>".format(books_list))