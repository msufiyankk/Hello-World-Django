from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world,name="sample"),
    path('product/', views.product_temp,name="product"),
    path('about/', views.about_us,name="about"),

]

