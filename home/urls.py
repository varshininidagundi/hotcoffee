
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path('services', views.services, name='services'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path("contact", views.contact, name='contact'),
    path("order", views.order, name='order')
]
