from django import forms
from django.forms import TextInput

from autoutilitare.models import Autoutilitare




class AutoutilitareForm(forms.ModelForm):
    class Meta:
        model = Autoutilitare
        fields = '__all__'

        widgets = {
            'model': TextInput(attrs={'placeholder':'Introduceti modelul autoutilitarei',
                                      'class':'form-control'}),
            'categorie': TextInput(attrs={'placeholder': 'Introduceti categoria autoutilitarei',
                                      'class': 'form-control'}),
            'an_fabricatie': TextInput(attrs={'placeholder': 'Introduceti anul de fabricatie al autoutilitarei',
                                          'class': 'form-control'}),
            'caroserie': TextInput(attrs={'placeholder': 'Introduceti caroseria autoutilitarei',
                                          'class': 'form-control'}),
            'combustibil': TextInput(attrs={'placeholder': 'Introduceti combustibilul autoutilitarei',
                                          'class': 'form-control'}),
            'putere': TextInput(attrs={'placeholder': 'Introduceti puterea autoutilitarei',
                                          'class': 'form-control'}),
            'capacitate_cilindrica': TextInput(attrs={'placeholder': 'Introduceti capacitatea colindrica a autoutilitarei',
                                       'class': 'form-control'}),
            'norma_poluare': TextInput(
                attrs={'placeholder': 'Introduceti norma de poluare a autoutilitarei',
                       'class': 'form-control'}),
            'greutate_maxima': TextInput(
                attrs={'placeholder': 'Introduceti greutatea maxima a autoutilitarei',
                       'class': 'form-control'}),
            'cutie_de_viteza': TextInput(
                attrs={'placeholder': 'Introduceti cutia de viteza a autoutilitarei',
                       'class': 'form-control'}),
            'numar_de_locuri': TextInput(
                attrs={'placeholder': 'Introduceti numarul de locuri a autoutilitarei',
                       'class': 'form-control'}),

        }