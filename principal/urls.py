from django.urls import path
from principal.views import home
from principal.views import  prueba


urlpatterns = [
    path("", home, name="home"),
    path("accounts/login", prueba, name="login"),
    # path("accounts/logout", name="logout"),
    
]



