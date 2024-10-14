from django import forms
from .models import Noticia, Categoria


class Formulario_Noticia(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Noticia
        fields = ["titulo", "contenido", "imagen", "categorias"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }



class Formulario_Modificar_Noticia(forms.ModelForm):
    categorias = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Noticia
        fields = ["titulo", "contenido", "imagen", "categorias"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "contenido": forms.Textarea(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }