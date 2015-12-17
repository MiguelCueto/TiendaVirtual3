from django import forms
from miapp3.models import Articulo

class ArticuloForm(forms.ModelForm):

	class Meta:
		model = Articulo
		fields = ('nombre','precio','tipo','foto',)
