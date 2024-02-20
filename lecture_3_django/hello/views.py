from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "hello/index.html")


def andre(request):
    return HttpResponse("Hello Andre!")


def david(request):
    return HttpResponse("Hello David!")


def greet(request, name: str):
    return render(request, "hello/greet.html",
                  {
                      "name": name.capitalize()
                  })
