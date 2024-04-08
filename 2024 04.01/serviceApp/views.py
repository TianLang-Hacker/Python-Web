from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def science(request):
    html='<html><body>你干嘛~哈哈~哎哟~</body><html>'
    return HttpResponse(html)