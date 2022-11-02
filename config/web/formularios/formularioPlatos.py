from django import forms

class FormularioPlatos(forms.Form):

    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postre')
    )

    nombre=forms.CharField(
        required=True,
        max_length=25,
        label="Nombre Plato",
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=True,
        max_length=10,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-select  mb-3'}),
        choices=PLATOS
    )
    descripcion=forms.CharField(
        required=True,
        max_length=25,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
