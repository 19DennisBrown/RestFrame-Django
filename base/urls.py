
from django.urls import path
from . import views



urlpatterns = [
  path('', views.view, name="view"),
  path('person/<int:id>/', views.personView, name="person"),
]