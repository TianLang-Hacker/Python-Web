from django.urls import path
from .import views
app_name='newsApp'
urlpatterns = [
    path('company/',views.company),
    path('industry/',views.industry),
    path('notice/',views.notice),
]