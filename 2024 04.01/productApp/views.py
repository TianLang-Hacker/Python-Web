from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def robot(request):
    html='<html><body>6</body><html>'
    return HttpResponse(html)

def monitoring(request):
    html='<html><body>1145</body><html>'
    return HttpResponse(html)

def face(request):
    html='<html><body>114514</body><html>'
    return HttpResponse(html)