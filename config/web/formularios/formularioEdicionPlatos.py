from django import forms

class FormularioEdicionPlatos(forms.Form):
    precioPlato=forms.CharField(
        required=True,
        max_length=10,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )