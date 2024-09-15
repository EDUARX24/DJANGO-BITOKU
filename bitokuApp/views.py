from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("<h2>Hola Tilines!</h2>")

def about(request):
    return HttpResponse("<h2>About!</h2>")

def maria(request):
    return HttpResponse("<h2>Hola Maria!</h2>")