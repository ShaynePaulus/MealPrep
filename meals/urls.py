from django.urls import path

from . import views

app_name = 'meals'
urlpatterns = [
    path('', views.Menu.as_view(), name='home'),

    path('recipes', views.RecipesView.as_view(), name='recipes'),
    path('recipe/', views.RecipeCreate.as_view(), name='recipe'),
    path('recipe-url/', views.RecipeUrlCreate.as_view(), name='recipe-url'),
    path('recipe/<int:pk>', views.Recipe.as_view(), name='recipe-view'),
    path('recipe/<int:pk>/update', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete', views.RecipeDelete.as_view(), name='recipe-delete'),

    path('menu', views.Menu.as_view(), name='menu'),
    path('grocery-list', views.GroceryList.as_view(), name='list'),
]