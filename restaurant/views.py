from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def display_menu_item(request, menu_item):
    return HttpResponse(f"<h2>{menu_item}</h2>")


def display_menu_item_by_id(request, item_id):
    return HttpResponse(f"<h2>Menu item ID: {item_id}</h2>")
