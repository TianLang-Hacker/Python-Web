from django.urls import path
from . import views
app_name='aboutApp'
urlpatterns = [
    path('survey/',views.survey),
    path('honor/',views.honor),
]