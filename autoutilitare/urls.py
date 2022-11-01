from django.urls import path

from autoutilitare import views

urlpatterns=[
    path('adauga_autoutilitare/', views.AutoutilitareCreateView.as_view(), name='creaza-auto'),
    path('lista_de_autoutilitare/', views.AutoutilitareListView.as_view(), name='lista-de-autoutilitare'),
    path('update_autoutilitare/<int:pk>/', views.AutoutilitareUpdateView.as_view(), name='update-autoutilitare'),
    path('stergere_autoutilitara/<int:pk>/', views.AutoutilitareDeleteView.as_view(), name='stergere-autoutilitara')
]