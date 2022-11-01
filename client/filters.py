import django_filters

from client.models import Client


class ClientFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='Nume')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Prenume')
    phone_number = django_filters.CharFilter(lookup_expr='icontains', label='Numar de telefon')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    driver_license = django_filters.CharFilter(lookup_expr='icontains', label='Permis de conducere')
    drivers_validity_license = django_filters.CharFilter(lookup_expr='icontains', label='Valabilitate permis')
    country_of_residence = django_filters.CharFilter(lookup_expr='icontains', label='Tara de rezidenta')



    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'driver_license', 'drivers_validity_license', 'country_of_residence',
                  'car']

    def __init__(self, *args, **kwargs):
        super(ClientFilter, self).__init__(*args, **kwargs)

        self.filters['first_name'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti numele'})
        self.filters['last_name'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti prenumele'})
        self.filters['phone_number'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti numarul de telefon'})
        self.filters['email'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti emailul'})
        self.filters['driver_license'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti seria de pe permis'})
        self.filters['drivers_validity_license'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti valabilitatea permisului de conducere'})
        self.filters['country_of_residence'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Introduceti tara de rezidenta'})