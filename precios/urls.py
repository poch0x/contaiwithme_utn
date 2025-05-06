from django.urls import path
from precios import views


urlpatterns = [
    path('', views.index, name="index"),
]
