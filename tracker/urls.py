from django.urls import path
from .import views

urlpatterns = [
    path('', views.list_food_items, name='list_food_items'),
    path('add/', views.add_food_item, name='add_food_item'),
    path('delete/<int:food_item_id>/', views.delete_food_item, name='delete_food_item'),
    path('reset/', views.reset_view, name='reset'),
    # path('')
]