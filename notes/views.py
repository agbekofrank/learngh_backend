from django.shortcuts import render

# Create your views here.


def home(req):

    context = {}

    return render(req, 'notes/home.html', context)
