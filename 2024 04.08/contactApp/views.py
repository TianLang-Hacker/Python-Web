from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def contact(request):  # 欢迎咨询
    html='<html><body>欢迎咨询</body></html>'
    return HttpResponse(html)
def recruit(request):  # 加入恒达
    html='<html><body>加入恒达</body></html>'
    return HttpResponse(html)