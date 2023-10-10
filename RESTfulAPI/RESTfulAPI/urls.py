"""
URL configuration for RESTfulAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dataTest import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/create/', views.menu_create, name='menu_create'),
    path('menu/<int:pk>',views.menu_select, name='menu_select'),
    path('menu/edit/<int:pk>/', views.menu_edit, name='menu_edit'),
    path('order_recode/', views.order_recode, name='order_recode'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
