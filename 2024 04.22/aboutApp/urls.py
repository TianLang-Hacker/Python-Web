from django.urls import path
from . import views
app_name='aboutApp'
urlpatterns = [
    path('survey/',views.survey,name='survey'), # 企业概况,name='survey'用于index.html逆向解析
    path('honor/',views.honor,name='honor'),    # 荣誉资质
]