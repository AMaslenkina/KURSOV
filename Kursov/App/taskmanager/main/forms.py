from django import forms


class FindProject(forms.Form):
    name = forms.CharField(label='Название проекта', max_length=50, required=False)

class FindPrice(forms.Form):
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2, required=False)

class FindEmpl(forms.Form):
    FIO = forms.CharField(label='ФИО', max_length=50)