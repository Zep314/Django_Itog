from django.urls import path
from .views import index, Recipes


urlpatterns = [
    path('', index, name='index'),
#    path('lastday/<int:client_id>/<int:days>', LastDay.as_view(), name='lastday'),
    path('recipes', Recipes.as_view(), name='recipes'),
    # path('product/', ProductView.as_view(), name='product_form'),
]
