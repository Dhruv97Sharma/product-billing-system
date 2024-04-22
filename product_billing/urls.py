from django.urls import path
from product_billing import views

urlpatterns = [
    path('products/', views.index, name='products'),
]