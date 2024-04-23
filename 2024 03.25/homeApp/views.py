from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    html='<html><body>Chicken you are so beautiful</body></html>'
    return HttpResponse(html)
