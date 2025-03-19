from django.urls import path
from . import views

urlpatterns = [
    path('',views.Base_page, name='base.html'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('show-recipes/', views.show_recipes, name='show_recipes'),
]
