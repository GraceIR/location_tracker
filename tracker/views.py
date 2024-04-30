from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'tracker/index.html')


def result(request):
    return render(request, 'tracker/result.html')