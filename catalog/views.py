from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    # catalog/product_list.html

# def index(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)


class ProductDetailView(DetailView):
    model = Product

# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
    # context = {'product': product}
    # return render(request, 'products_detail.html', context)
