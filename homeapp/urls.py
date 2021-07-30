from django.contrib import admin
from django.urls import path, include
from homeapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('test/', views.test, name='test'),
    path('test/<str:title>/', views.test_package, name='test_package'),

    path('offers/', views.offers, name='offers'),
    path('faq/', views.faq, name='faq'),
    path('packages/', views.packages, name='packages'),
    path('centers/', views.centers, name='centers'),

]
