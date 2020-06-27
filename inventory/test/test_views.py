from django.test import RequestFactory
from django.urls import reverse
from inventory.views import list_product, add_product, generate_csv
import pytest
from django.contrib.auth.models import AnonymousUser
from inventory.models import MasterProductsConfigurable
from django.test import Client

@pytest.mark.django_db
class TestView:
    def test_list_product(self):
        product = MasterProductsConfigurable.objects.create(
            model = 'YR-MODEL-20',
            sku = 'YR-45655',
            name = 'polera mujer' ,
            price = '6990',
            attribute_color = 'blanca',
        ).save()
        product2 = MasterProductsConfigurable.objects.create(
            model = 'YR-MODEL-20',
            sku = 'YR-45656',
            name = 'polera mujer' ,
            price = '6990',
            attribute_color = 'negra',
        ).save()
        path = reverse('list_product')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = list_product(request)
        assert response.status_code == 200
    
    def test_add_product(self):
        path = reverse('add_product')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        product =  Client()
        product.post(path,{
            'model' : 'YR-MODEL-20',
            'sku' : 'YR-45655',
            'name' : 'polera mujer' ,
            'price' : '6990',
            'attribute_color' : 'blanca'})
        response = add_product(request)
        assert response.status_code == 200

    def test_list_product(self):
        product = MasterProductsConfigurable.objects.create(
            model = 'YR-MODEL-20',
            sku = 'YR-45655',
            name = 'polera mujer' ,
            price = '6990',
            attribute_color = 'blanca',
        ).save()
        path = reverse('report')
        request = RequestFactory().get(path)
        request.user = AnonymousUser()
        response = generate_csv(request)
        assert response.status_code == 200