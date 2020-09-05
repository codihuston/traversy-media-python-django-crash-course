from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
  # index: /polls
  path('', views.index, name='index'),
]