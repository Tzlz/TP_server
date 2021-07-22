from django.urls import include, path

from api import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register)]
