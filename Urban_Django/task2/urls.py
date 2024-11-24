from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.func, name='func'),
    path('class/', views.func2, name='func2'),
    path('', views.func3, name='func3'),
]