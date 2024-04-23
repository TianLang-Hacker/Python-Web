from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def company(request):
    html='<html><body>6</body><html>'
    return HttpResponse(html)

def industry(request):
    html='<html><body>1145</body><html>'
    return HttpResponse(html)

def notice(request):
    html='<html><body>114514</body><html>'
    return HttpResponse(html)