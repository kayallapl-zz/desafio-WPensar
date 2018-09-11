from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmbuy.html/', views.buy_product, name='confirmbuy'),
]
