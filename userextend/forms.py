from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput


class UserExtendForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Introduceti numele',
                                           'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Introduceti prenumele',
                                          'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Introduceti emailul',
                                       'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Introduceti username',
                                         'class': 'form-control'})
        }

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Introduceti parola'}),
        self.fields['password2'].widget.attrs.update({'class': 'form-control',
                                                      'placeholder': 'Confirmati parola'}),


class AuthenticationNewForm(AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Introduceti parola'})


class PasswordResetNewForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your email'})


class SetPasswordNewForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update( {'class': 'form-control',
                                                           'placeholder': 'Please enter your password'})
        self.fields['new_password2'].widget.attrs.update( {'class': 'form-control',
                                                           'placeholder': 'Please enter your password confirmation'})

