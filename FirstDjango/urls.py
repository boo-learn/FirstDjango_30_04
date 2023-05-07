from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('item/<int:id>/', views.item_page, name="item-detail"),
    path('items/', views.items_list, name="items-list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

