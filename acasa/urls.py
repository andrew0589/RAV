from django.urls import path

from acasa import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name='acasa')
]
