from django.shortcuts import render

def home(request):
    return render(request, 'covid_survey/home.html', {})

