from django.urls import path
from contratos import views

urlpatterns = [
    path('', views.index, name="index"),
]
