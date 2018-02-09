from django.forms import forms
from products.models import Image


class UploadFileForm(forms.Form):
    class Meta:
        model = Image
        fields = ('product_image', 'product_image.name',)
        print('fd')
