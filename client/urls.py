from django.urls import path

from client import views

urlpatterns = [
    path('creaza_client/', views.ClientCreateView.as_view(), name='creaza-client'),
    path('lista_de_clienti/', views.ClientListView.as_view(), name='lista-de-clienti'),
    path('update_client/<int:pk>/', views.ClientUpdateView.as_view(), name='update-client'),
    path('delete_client/<int:pk>/', views.ClientDeleteView.as_view(), name='delete-client'),
    path('detalii_client/<int:pk>/', views.ClientDetailView.as_view(), name='detalii-client')
]