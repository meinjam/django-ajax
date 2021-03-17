from django.shortcuts import render, redirect
from .models import *
from django.views import View


def homepage(request):
    return render(request, "index.html")
