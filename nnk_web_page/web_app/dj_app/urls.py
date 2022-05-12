from . import views
from django.urls import path

urlpatters=[
    path('', views.MainView)
]