from django.urls import path
from .import views
app_name='productApp'
urlpatterns = [
    path('robot/',views.robot),
    path('monitoring/',views.monitoring),
    path('face/',views.face),
]