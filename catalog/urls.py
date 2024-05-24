# from django.urls import path, include
# from catalog.apps import CatalogConfig
#
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path('', include('catalog.urls', namespace='catalog')),
# ]
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home,contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts')
]