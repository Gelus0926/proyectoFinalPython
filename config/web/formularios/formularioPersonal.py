from django import forms


class FormularioPersonal(forms.Form):

    CARGO=(
        (1, 'Cocinero'),
        (2, 'Ayudante'),
        (3, 'Mesero'),
        (4, 'Administrador')
    )

    nombres=forms.CharField(
        required=True,
        max_length=25,
        label="Nombres Del Empleado",
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellidos=forms.CharField(
        required=True,
        max_length=25,
        label="Apellidos Del Empleado",
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    foto=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    cargo=forms.ChoiceField(
        required=True,
        label="Cargo Del Empleado",
        widget=forms.Select(attrs={'class':'form-select  mb-3'}),
        choices=CARGO
    )
    salario=forms.CharField(
        required=True,
        max_length=10,
        label="Salario Del Empleado",
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    contacto=forms.CharField(
        required=True,
        max_length=10,
        label="Contacto Del Empleado",
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
