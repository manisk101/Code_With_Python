from django.urls import path
from .import views
[
    path("",views.index),
    path('counter',views.counter),
]