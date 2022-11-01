from django.urls import path

from despre_noi import views

urlpatterns = [
    path('despre_noi/', views.HomeTemplateView.as_view(), name='despre-noi')
]