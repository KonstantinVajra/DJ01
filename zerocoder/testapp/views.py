from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testapp(request):
    return HttpResponse("<h1>  Страница Test!</h1>")


# Create your views here.