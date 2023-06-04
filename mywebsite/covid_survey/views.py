from django.shortcuts import render
from .forms import CovidQuestionnaireForm


def home(request):
    form = CovidQuestionnaireForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    return render(request, 'covid_survey/home.html', {'form': form})

