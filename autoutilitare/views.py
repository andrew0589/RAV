from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from autoutilitare.forms import AutoutilitareForm
from autoutilitare.models import Autoutilitare


class AutoutilitareCreateView(LoginRequiredMixin, CreateView):
    template_name = 'autoutilitare/creaza_autoutilitare.html'
    model = Autoutilitare
    form_class = AutoutilitareForm
    success_url = reverse_lazy('acasa')


class AutoutilitareListView(LoginRequiredMixin, ListView):
    template_name = 'autoutilitare/lista_de_autoutilitare.html'
    model = Autoutilitare
    context_object_name = 'all_autoutilitare'


class AutoutilitareUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'autoutilitare/update_autoutilitare.html'
    model = Autoutilitare
    form_class = AutoutilitareForm
    success_url = reverse_lazy('acasa')


class AutoutilitareDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'autoutilitare/stergere_autoutilitara.html'
    model = Autoutilitare
    success_url = reverse_lazy('lista-de-autoutilitare')
