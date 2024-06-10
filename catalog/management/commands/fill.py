from django.core.management import BaseCommand

# import catalog.json
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():

    @staticmethod
    def json_read_products():

    def handle(self, *args, **options):
        product_for_create = []   # Создайте списки для хранения объектов
        category_for_create = []  # Создайте списки для хранения объектов

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(title="", description="")
            )
        Category.objects.bulk_create(category_for_create)  # Создаем объекты в базе с помощью метода bulk_create()

        for product in Command.json_read_products():
            product_for_create.append(
                Product(title="", description="", category="pk(1:2)", price=int)
            Category.title["смартфоны"] = Category.objects.get(pk=1),
            Category.title["телевизоры"] = Category.objects.get(pk=2),
            title = "")
            )

            Product.objects.bulk_create(product_for_create) # Создаем объекты в базе с помощью метода bulk_create()
