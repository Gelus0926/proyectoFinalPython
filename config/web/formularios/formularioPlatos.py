from django import forms

class FormularioPlatos(forms.Form):

    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postre')
    )

    nombrePlato=forms.CharField(
        required=True,
        max_length=25,
        label="Nombre Plato",
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografiaPlato=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precioPlato=forms.CharField(
        required=True,
        max_length=10,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipoPlato=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select  mb-3'}),
        choices=PLATOS
    )
    descripcionPlato=forms.CharField(
        required=True,
        max_length=100,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
