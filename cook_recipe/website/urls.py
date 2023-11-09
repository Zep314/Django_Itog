from django.urls import path
from .views import index, Recipes, RecipeDetail, RecipeDelete


urlpatterns = [
    path('', index, name='index'),
    path('recipes/', Recipes.as_view(), name='recipes'),
    path('recipe/', RecipeDetail.as_view(), name='recipe_form'),
    path('delete/', RecipeDelete.as_view(), name='recipe_delete'),
]
