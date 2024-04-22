from django.shortcuts import render
from product_billing.models import Product
from product_billing.forms import ProductSelectionForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ProductSelectionForm(request.POST)
        if form.is_valid():
            selected_products = form.cleaned_data['products']
            # Process selected products
    else:
        form = ProductSelectionForm()
    products = Product.objects.all()
    return render(request, 'product_billing/index.html', {'products': products})