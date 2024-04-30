
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path('services/', views.services, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path("contact", views.contact, name='contact'),
    path("order", views.order, name='order')
]
