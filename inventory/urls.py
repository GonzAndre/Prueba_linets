from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.list_product, name="list_product"),
    path('report', views.generate_csv, name="report"),
    path('add_product', views.add_product, name="add_product"),
]