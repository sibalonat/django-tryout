from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marin', views.marin, name='marin'),
    path('<str:name>', views.fry, name='fry'),
]