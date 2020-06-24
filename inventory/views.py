from django.shortcuts import render
from inventory.models import MasterProductsConfigurable
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import csv
from django.utils import timezone
import datetime
from django.db.models import Count

# Create your views here.

def generate_csv(request):
    products = MasterProductsConfigurable.objects.all()
    time = str(timezone.now())
    name = 'productos-' + time[:10] + '.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + '"'+ name + '"'
    writer = csv.writer(response)
    writer.writerow(['model | name | price | configurations_variations'])

    lista = []
    
    product = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model')
    prod_first = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model').earliest('model','sku')
    prod_last = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model').latest('model','-sku')

    item_model = prod_first['model']
    row = prod_first['model'] + '|' + prod_first['name'] + '|' + prod_first['price'] + '| sku=' + prod_first['sku']

    for item in product:
        if  item_model == item['model']:
            row = row + '| sku=' + item['sku'] + ', color=' + item['attribute_color']
            if item['sku'] == prod_last['sku']:
                writer.writerow([row])

        else:
            item_model = item['model']
            writer.writerow([row])
            row = item['model'] + '|' + item['name'] + '|' + item['price'] + '| sku=' + item['sku'] + ', color=' + item['attribute_color']

    return response

def home(request):
    return render(request, 'home.html')

