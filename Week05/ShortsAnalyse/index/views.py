from django.shortcuts import render
from django.http import HttpResponse
from .models import Shorts

def index(request):
    return HttpResponse('Hello Django')

def shorts(request):
    n=Shorts.objects.all()
    return  render(request,'shortslist.html',locals())