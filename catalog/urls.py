# from django.urls import path, include
# from catalog.apps import CatalogConfig
# from catalog.views import index
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path('', include('catalog.urls', namespace='catalog')),
# ]
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, products_detail

app_name = CatalogConfig.name

# urlpatterns = [
#     path('', home, name='home'),
#     path('contacts/', contacts, name='contacts')
# ]


urlpatterns = [
    path('', index, name='product_list'),
    path('catalog/<int:pk>/', products_detail, name='products_detail')
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('products.urls', namespace='products'))
# ]