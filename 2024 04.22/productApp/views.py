from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def  robot(request):    # 机器人
    html='<html><body>机器人</body></html>'
    return HttpResponse(html)
def monitoring(request): # 智能监控
    html='<html><body>智能监控</body></html>'
    return HttpResponse(html)
def face(request):    # 人脸识别
    html='<html><body>人脸识别</body></html>'
    return HttpResponse(html)