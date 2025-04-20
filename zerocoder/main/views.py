from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def new(request):
    return render(request, 'main/new.html')

def romeiro_view(request):
    return render(request, 'main/romeiro.html')

def empty_island_view(request):
    return render(request, 'main/empty_island.html')

def light_path_view(request):
    return render(request, 'main/light_path.html')

def sunset_view(request):
    return render(request, 'main/sunset.html')