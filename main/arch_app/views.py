from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render

# Create your views here.
def index(request):
    response = "This should be JSON!"
    return HttpResponse(response)