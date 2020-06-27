from inventory.models import MasterProductsConfigurable
from django.shortcuts import get_object_or_404
import pytest

@pytest.mark.django_db
class TestModels:

    def test_product(self):
        product = MasterProductsConfigurable.objects.create(
            model = 'YR-MODEL-20',
            sku = 'YR-45654',
            name = 'polera mujer' ,
            price = '6990',
            attribute_color = 'blanca',
        ).save()

        assert get_object_or_404(MasterProductsConfigurable, sku='YR-45654')
    
    def test_product_incorrect(self):
        product = MasterProductsConfigurable.objects.create(
            model = 'YR-MODEL-20',
            sku = 'YR-45655',
            name = 'polera mujer' ,
            price = 6990,
            attribute_color = 19990,
        ).save()

        assert get_object_or_404(MasterProductsConfigurable, sku='YR-45655')