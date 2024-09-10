from django.shortcuts import render
from django.http import HttpResponse
from .stationscan import ScanBus

def home(request):
    return render(request, 'top/top.html')

def CallScriptView(request):
    result = ScanBus()
    return HttpResponse(result)