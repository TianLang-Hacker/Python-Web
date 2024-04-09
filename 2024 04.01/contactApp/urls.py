from django.urls import path
from .import views
app_name='contactApp'
urlpatterns = [
    path('contact/',views.contact),
    path('recruit/',views.recruit),
   
]