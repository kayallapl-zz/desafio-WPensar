from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^products$', views.show_products_list, name="show_products_list"),
    url(r'^search$', views.search, name="search"),
    url(r'^searchresult$', views.searchresult, name="searchresult"),
    url(r'^register$', views.register, name="register"),
    url(r'^addproduct$', views.addproduct, name="addproduct"),
]