from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
