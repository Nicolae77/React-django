from django.urls import path
from . import views

urlpatterns =[
    path('api/', views.getRoutes, name='routes'),
]