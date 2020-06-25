from django.shortcuts import render
from inventory.models import MasterProductsConfigurable
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import csv
from django.utils import timezone
from inventory.forms import MasterProductForm

# Create your views here.

def generate_csv(request):

    # definir nombre del archvio csv
    time = str(timezone.now())
    name = 'productos-' + time[:10] + '.csv'
    # iniciamos el archivo csv con response, para que se descargue
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + '"'+ name + '"'
    writer = csv.writer(response)
    # definir los encabezados de la tabla
    writer.writerow(['model | name | price | configurations_variations'])
    # Consultamos todos los objetos de MasterProductsConfigurable como diccionario
    product = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model')
    # obtenemos el primer objeto de product, para iniciar con esa variable
    prod_first = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model').earliest('model','sku')
    # obtenemos el ultimo objeto de product, de este nececitamos el sku(id), para saber cuando terminar la tabla
    prod_last = MasterProductsConfigurable.objects.values('model','sku','price','name','attribute_color').order_by('model').latest('model','-sku')

    item_model = prod_first['model']
    row = prod_first['model'] + '|' + prod_first['name'] + '|' + prod_first['price'] + '| sku=' + prod_first['sku']

    # comenzamos el for, con la variable item_model como objeto inicial.
    for item in product:
        # mientras los modelos sean iguales, los colores se iran agregando a la linea
        if  item_model == item['model']:
            row = row + '| sku=' + item['sku'] + ', color=' + item['attribute_color']
            # consultamos el sku del ultimo objeto para saber cuando terminar de escribir en el csv
            if item['sku'] == prod_last['sku']:
                writer.writerow([row])

        else:
            # se cambia la variable al modelo que corresponde en el for
            item_model = item['model']
            # cuando el modelo es distinto, se escribe la linea del modelo anterior, con todos sus colores
            writer.writerow([row])
            # se inicia la variable row con los nuevos datos del modelo
            row = item['model'] + '|' + item['name'] + '|' + item['price'] + '| sku=' + item['sku'] + ', color=' + item['attribute_color']

    return response

def list_product(request):
    data = {}
    object_list = MasterProductsConfigurable.objects.all().order_by('model')
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page')
    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)
    return render(request, 'list_product.html', data)

def add_product(request):
    data = {}
    if request.method == "POST":
        data['product'] = MasterProductForm(request.POST)
        if data['product'].is_valid():
            data['product'].save()
            return redirect('list_product')
    else:
        data['product'] = MasterProductForm()
    
    return render(request, 'add_product.html',data)