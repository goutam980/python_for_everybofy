
from django.urls import path
from . import views

urlpatterns=[
    path("isit/",views.index,name="name"),
]