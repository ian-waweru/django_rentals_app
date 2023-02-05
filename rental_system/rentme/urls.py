from django.urls import path
from . import views

# url patterns for rentme app only

app_name = "rentme"

urlpatterns = [
    path('', views.index, name='index'),
]