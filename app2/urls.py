from django.urls import path
from app2 import views

urlpatterns = [
    path('form/', views.employeeinput),
]
