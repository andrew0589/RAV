from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from client.filters import ClientFilter
from client.models import Client
from client.forms import ClientForm, UpdateClientForm


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'client/creaza_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('acasa')
    permission_required = 'client.add_client'

    def get_context_data(self, **kwargs):
        data = super(ClientCreateView, self).get_context_data(**kwargs)
        clients = Client.objects.all()
        data['all_clients'] = clients

        return data


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'client/lista_de_clienti.html'
    model = Client
    context_object_name = 'all_clients'
    permission_required = 'client.view_list_of_clients'


    def get_context_data(self, **kwargs):
        data = super(ClientListView, self).get_context_data(**kwargs)
        clients = Client.objects.all()
        my_filter = ClientFilter(self.request.GET, queryset=clients)
        clients = my_filter.qs
        data['all_clients'] = clients
        data['my_filter'] = my_filter

        return data


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'client/update_client.html'
    model = Client
    form_class = UpdateClientForm
    success_url = reverse_lazy('acasa')
    permission_required = 'client.update_client'


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'client/stergere_client.html'
    model = Client
    success_url = reverse_lazy('lista-de-clienti')
    permission_required = 'client.delete_client'


class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'client/detalii_client.html'
    model = Client
    permission_required = 'client.view_client'
