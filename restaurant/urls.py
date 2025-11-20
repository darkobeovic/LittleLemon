from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Dynamic routes
    path('menu/<str:menu_item>/', views.display_menu_item, name='display-menu'),
    path('menu/id/<int:item_id>/',
         views.display_menu_item_by_id, name='display-menu-id'),
]
