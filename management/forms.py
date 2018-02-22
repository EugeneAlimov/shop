from django import forms
from products.models import Image


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['product_image', 'name_of_product_image']
