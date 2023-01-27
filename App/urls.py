from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('days', views.days, name='days'),
    path('year', views.year_holidays, name='year')
]