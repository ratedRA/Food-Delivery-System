from .views import*
from django.urls import path, include

urlpatterns = [
    path('f/', food_providers, name='home_page'),
    path('', all_res, name='res_names'),
    path('order/', show_navigation, name='navigate'),
    path('restaurants/', ListResView.as_view(), name="Restaurants"),
    path('Delivery/', ListDelView.as_view(), name="Delivery"),
]