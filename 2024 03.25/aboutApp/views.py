from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def survey(request):
    html='<html><body>Cai Xukun</body></html>'
    return HttpResponse(html)

def honor(request):
    html='<html><body>6</body></html>'
    return HttpResponse(html)