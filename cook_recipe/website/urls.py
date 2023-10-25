from django.urls import path
from .views import index, Home


urlpatterns = [
    path('', index, name='index'),
#    path('lastday/<int:client_id>/<int:days>', LastDay.as_view(), name='lastday'),
    path('home', Home.as_view(), name='home'),
    # path('product/', ProductView.as_view(), name='product_form'),
]
