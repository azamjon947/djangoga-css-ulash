
from django.urls import path
from .views import home, about, section, web, navbar, footer

urlpatterns = [
    path('', home),
    path('about/', about),
    path('section/', section),
    path('web/', web),
    path('navbar/', navbar),
    path('footer/', footer),
 
]