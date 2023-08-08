from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# MVT - Model, View, Template
#    database, Business logic, HTML files.


def root(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        """<h1 style="color:teal">Welcome to the Web ML</h1>"""
    )

def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")

def user(request: HttpRequest) -> HttpResponse:
    username = request.GET["username"]
    return render(request, 'user.html', {'name': username})