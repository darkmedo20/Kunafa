
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu_items/', views.MenuItemsView.as_view()),
    path('<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('about/', views.about, name="about"),
    path('menu/<int:pk>/', views.menuItem, name="menuItem"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('bookings/', views.reservations, name="reservations"),
    path('', views.home, name="home"),

]