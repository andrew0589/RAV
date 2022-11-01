from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rentavan.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm

    # success_url = reverse_lazy('acasa')

    def form_valid(self, form):
        # if form.is_valid() and not form.errors:
        #     new_user = form.save(commit=False)
        #     new_user.first_name = new_user.first_name.title()
        #     new_user.last_name = new_user.last_name.title()
        #
        #     new_user.save()
        #
        #     subject = 'Cont nou!'
        #     message = f'Salutare, {new_user.first_name} {new_user.last_name}, Contul tau a fost creat.'
        #     from_email = EMAIL_HOST_USER
        #     to_email = [new_user.email]
        #     send_mail(subject, message, from_email, to_email)
        #

        if form.is_valid() and not form.errors:
            new_user = form.save()

            details_user = {
                'full_name': new_user,
                'username': new_user.username
            }

            subject = 'Creare cont nou!'
            message = get_template('userextend/mail_create_new_user.html').render(details_user)
            from_email = EMAIL_HOST_USER
            to_email = [new_user.email]

            email = EmailMessage(subject, message, from_email, to_email)
            email.content_subtype = 'html'
            email.send()

        return redirect('acasa')
