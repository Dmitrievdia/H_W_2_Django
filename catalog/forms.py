# from django.forms import ModelForm
from django import forms
from .models import Product
# from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                       'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ['title', 'description', 'avatar', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите наименование продукта"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта"
        })

        self.fields["avatar"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Добавьте изображение продукта"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Укажите категорию продукта"
        })

        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Укажите цену продукта"
        })

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if any(word in title.lower() for word in self.forbidden_words):
            raise forms.ValidationError("Название не должно содержать запрещенные слова.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if any(word in description.lower() for word in self.forbidden_words):
            raise forms.ValidationError("Описание не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")

        return price

