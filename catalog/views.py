from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'

# def index(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products_detail.html'
# def products_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
    # context = {'product': product}
    # return render(request, 'products_detail.html', context)


class ProductCreateView(CreateView):
    model = Product
    # fields = ("title", "description", "avatar", "category", "price")
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    # fields = ("title", "description", "avatar", "category", "price")
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


