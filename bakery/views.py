from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from . import serializers
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .forms import BookingForm


import datetime
from datetime import datetime, date, time

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)  # Bind the form to POST data
        if form.is_valid():  # Validate the form
            form.save()  # Save the validated data to the database
            #return redirect('success_page')
    else:
        form = BookingForm()  # Create an empty form for GET requests
    return render(request, 'book.html', {'form': form})

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_data})

def menuItem(request, pk):
    # Fetch the specific menu item based on the provided ID
    menu_item = get_object_or_404(Menu, id=pk)
    
    # Pass the menu item to the template
    return render(request, 'menu_item.html', {"menu_item": menu_item})
    