from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delete/<int:pk>/', views.delete),
    path('deleteall/', views.delete_all),
    path('register/', views.register),
    path('created_account/', views.created_account),
]