from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.get_product, name = 'get_product')
]
