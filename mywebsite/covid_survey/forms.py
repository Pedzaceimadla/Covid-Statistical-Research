from django import forms
from .models import CovidQuestionnaire

class CovidQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = CovidQuestionnaire
        fields = ['infected', 'immunized']
        widgets = {
            'infected': forms.CheckboxInput(attrs={'class': 'forms-check-input'}),
            'immunized': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
