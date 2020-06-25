from django.forms import ModelForm
from inventory.models import MasterProductsConfigurable
from django import forms

class MasterProductForm(ModelForm):
    class Meta:
        model = MasterProductsConfigurable
        fields = ['model','sku', 'name','price','attribute_color']
        labels = {
            'model': 'Modelo',
            'sku': 'Sku',
            'name': 'Nombre',
            'price': 'Precio',
            'attribute_color': 'Color',
        }
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese modelo'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese identificador'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre producto'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese precio'}),
            'attribute_color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese color'}),
        }