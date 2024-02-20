from django.shortcuts import render
from datetime import date

# Create your views here.


def index(request):
    return render(request,
                  'newyear/index.html',
                  {'isNewYear': date.today().month == 1 and date.today().day == 1})
