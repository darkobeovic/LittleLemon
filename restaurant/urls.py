from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Rutas dinámicas antiguas (las dejamos)
    path('menu/<str:menu_item>/', views.display_menu_item, name='display-menu'),
    path('menu/id/<int:item_id>/',
         views.display_menu_item_by_id, name='display-menu-id'),

    # --- API Menu ---
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(),
         name='single-menu-item'),
]
