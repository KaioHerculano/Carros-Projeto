from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de $20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Carros com o ano abaixo do ano de 1975 não podem ser comercializados!')
        return factory_year
    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        minimal_len_char = 7
        if len(plate or ()) < minimal_len_char:
            raise forms.ValidationError('A placa deve ter no minimo '+str(minimal_len_char)+' caracteres!')
        return plate