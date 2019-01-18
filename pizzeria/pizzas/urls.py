from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('pizzas/',views.pizzas,name='pizzas'),
    re_path('pizzas/(\d+)/',views.pizza,name='pizza'),
    path('new_pizza/',views.new_pizza),
    re_path('new_topping/(\d+)/',views.new_topping),
    re_path('edit_topping/(\d+)/',views.edit_topping),
]
