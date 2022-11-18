from django import forms

class FormularioEmpleados(forms.Form):
    Empleados=(
        (1, 'Mesero'),
        (2, 'Cocinero'),
        (3, 'Cajero'),
        (4, 'Asistente Cocina')
    )
    nombre=forms.CharField(
        label="Nombre del empleado",
        required=True,
        max_length=40,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    salario=forms.CharField(
        required=True,
        max_length=200,
        widget=forms.NumberInput(attrs={'class':'form-control mb3'})
    )
    direccion=forms.CharField(
        required=True,
        max_length=40,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    telefono=forms.CharField(
        required=True,
        max_length=14,
        widget=forms.NumberInput(attrs={'class':'form-control mb3'})
    )
    tipoEmpleado=forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=Empleados
    )