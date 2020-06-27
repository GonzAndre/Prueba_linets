from django.urls import reverse, resolve

class TestUrls:
    def test_list_products(self):
        path = reverse('list_product')
        assert resolve(path).view_name == 'list_product'

    def test_generate_csv(self):
        path = reverse('report')
        assert resolve(path).view_name == 'report'