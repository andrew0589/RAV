from django import forms
from django.forms import TextInput, DateInput, Select

from client.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'driver_license', 'drivers_validity_license',
                  'country_of_residence', 'car']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                           'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name',
                                          'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number',
                                             'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter your email',
                                      'class': 'form-control'}),
            'driver_license': TextInput(attrs={'placeholder': 'Please enter your driver license',
                                               'class': 'form-control'}),
            'drivers_validity_license': DateInput(attrs={'class': 'form-control',
                                                         'type': 'date'}),
            'country_of_residence': TextInput(attrs={'placeholder': 'Please enter your country of residence',
                                                     'class': 'form-control'}),
            # 'start_date': DateInput(attrs={'class': 'form-control',
            #                                'type': 'date'}),
            # 'end_date': DateInput(attrs={'class': 'form-control',
            #                              'type': 'date'}),
            'car': Select(attrs={'class': 'form-select'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        all_clients = Client.objects.all()
        for client in all_clients:
            if client.first_name == cleaned_data['first_name'] and client.last_name == cleaned_data['last_name']:
                msg = f'Acest nume {cleaned_data["first_name"]} si acest prenume {cleaned_data["last_name"]} exista in baza de date'
                self._errors['first_name'] = self.error_class([msg])

        # if cleaned_data['start_date'] > cleaned_data['end_date']:
        #     msg = f'Start date is older than end date'
        #     self._errors['start_date'] = self.error_class([msg])

        return cleaned_data


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'driver_license', 'drivers_validity_license',
                  'country_of_residence', 'car']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name',
                                           'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name',
                                          'class': 'form-control'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number',
                                             'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Please enter your email',
                                      'class': 'form-control'}),
            'driver_license': TextInput(attrs={'placeholder': 'Please enter your driver license',
                                               'class': 'form-control'}),
            'drivers_validity_license': DateInput(attrs={'class': 'form-control',
                                                         'type': 'date'}),
            'country_of_residence': TextInput(attrs={'placeholder': 'Please enter your country of residence',
                                                     'class': 'form-control'}),
            # 'start_date': DateInput(attrs={'class': 'form-control',
            #                                'type': 'date'}),
            # 'end_date': DateInput(attrs={'class': 'form-control',
            #                              'type': 'date'}),
            'car': Select(attrs={'class': 'form-select'})
        }