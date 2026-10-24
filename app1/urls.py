from django.urls import path
from app1 import views

urlpatterns = [
    path('school/', views.school),
    path('form/', views.studentinputview),
]
