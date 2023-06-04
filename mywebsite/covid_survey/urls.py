
from django.urls import path
from covid_survey.views import home

urlpatterns = [
    path('', home, name='home'),


]
