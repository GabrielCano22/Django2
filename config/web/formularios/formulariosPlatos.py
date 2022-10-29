from django import forms



class FormularioPlatos(forms.Form):

    Platos=(
        (1,'Entradas'),
        (2,'Plato Fuerte'),
        (3,'Postre')
    )

    nombre=forms.CharField(
        required=True,
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )

    fotografia=forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=Platos
    )
    descripcion=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )