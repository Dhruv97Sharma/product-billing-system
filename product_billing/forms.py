# forms.py
from django import forms
from product_billing.models import Product

class ProductSelectionForm(forms.Form):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple)
