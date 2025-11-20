from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # --- API Menu (según el enunciado) ---
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>/', views.SingleMenuItemView.as_view(),
         name='single-menu-item'),

    # --- Rutas dinámicas antiguas (comentadas porque causan conflicto)
    # path('menu/<str:menu_item>/', views.display_menu_item, name='display-menu'),
    # path('menu/id/<int:item_id>/', views.display_menu_item_by_id, name='display-menu-id'),
]
