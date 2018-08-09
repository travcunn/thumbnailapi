from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def convert_image(request):
    return render(request, 'convert_image.html')
