from django.urls import path
from . import views

urlpatterns=[
    path("home/",views.index,name="index"),
    path("v1/",views.v1,name="view v1"),
]
