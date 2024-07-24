from django.shortcuts import render
from catalog.models import Product, Category


# def home(request):
#     return render(request, 'home.html')
#
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}): {message}')
#     return render(request, 'contacts.html')

# def index(request):
#     return render(request, 'base.html')


# def index(request):
#     products_list = Product.objects.all()
#     context = {"odject_list": products_list}
#     return render(request, 'base.html', context)

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base.html', context)

# from django.shortcuts import render
# kkk

