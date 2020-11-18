from django import forms
from .models import ClassesFichaDND

class ClasseFichaDNDDSelectForm(forms.ModelForm):

    class Meta:
        model = ClassesFichaDND
        fields = ['classe','ficha']