from django.urls import path

from termeni import views

urlpatterns = [
    path('termeni_si_conditii/', views.HomeTemplateView.as_view(), name='termeni')
]
