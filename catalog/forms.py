from django import forms

from catalog.models import Product
from version.forms import StyleFormMixin

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                   'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        if any(word in cleaned_data for word in forbidden_words):
            raise forms.ValidationError('Нельзя использовать запрещенные слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        if any(word in cleaned_data for word in forbidden_words):
            raise forms.ValidationError('Нельзя использовать запрещенные слова')
        return cleaned_data


