from .models import TrainerModel
from django import forms

class TrainerForm(forms.ModelForm):
    class Meta:
        model=TrainerModel
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'})
        }