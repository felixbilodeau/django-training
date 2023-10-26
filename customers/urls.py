from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_customer, name='customer-add'),
    path('<int:pk>/', views.update_customer, name='customer-update'),
]
