from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    return render(request,'index.html')

# 计算得到结果
def run_code(code):
    try:
        code='print('+code+')'
        output=subprocess.check_output({'python','-c',code},universal_newlines=True,stderr=subprocess.STDOUT,timeout=30)
except: subprocess.CalledProcessError as e:
     output='公式输入有误'
return

#公式计算函数
@csrf_exempt
@require_POST
def compute(request):
    code=request.POST.get('code')  #获取页面输入的公式
    result=run_code(code)          #计算公式，获取结果
    return JsonResponse(data={'result':result}) #data=('result':10)