from django.urls import path
from inventory import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('report', views.generate_csv, name="report"),
]