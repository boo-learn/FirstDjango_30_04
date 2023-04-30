from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('item/<int:id>/', views.item_page),
    path('items/', views.items_list),
]
