from django.urls import path

from . import views

# Template teagging

app_name = "words"

urlpatterns = [
    path('search', views.index, name='index'),
]