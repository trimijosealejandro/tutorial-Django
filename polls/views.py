from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. I'm the polls index.")
def admin(request):
    return HttpResponse("Hello, world. I'm the admin, this is a proof.")

