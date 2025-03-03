"""
URL configuration for Kunafa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from bakery import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bakery/menu/', include('bakery.urls')),
    path('bakery/drink/', include('bakery.urls')),
    path('bakery/booking/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('menu_items/', include('bakery.urls')),
    path('', include('bakery.urls')),
    path('menu/', views.menu),
]
