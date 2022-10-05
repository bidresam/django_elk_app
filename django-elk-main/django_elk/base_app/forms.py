from django import forms

class CityAddForm(forms.Form):
    city_name = forms.CharField(label='City')
    city_population = forms.IntegerField(label='Population', min_value=1)
