from rest_framework import viewsets, generics
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# --- Vistas HTML para rutas estáticas ---


def index(request):
    return render(request, 'index.html')


def display_menu_item(request, menu_item):
    return HttpResponse(f"<h2>{menu_item}</h2>")


def display_menu_item_by_id(request, item_id):
    return HttpResponse(f"<h2>Menu item ID: {item_id}</h2>")


# --- Vistas del API REST Framework ---

# GET (lista), POST (crear)

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# GET (single), PUT, DELETE


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
