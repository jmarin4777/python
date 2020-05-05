from django import forms
from .models import Show

class DateInput(forms.DateInput):
    input_type = 'date'

class addShow(forms.Form):
    title = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'title',
            'name': 'title',
        }
    ))
    network = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control ',
            'id': 'network',
            'name': 'network',
        }
    ))
    release_date = forms.DateField(required=False, widget=DateInput(
        attrs={
            'class': 'form-control ',
            'id': 'release_date',
            'name': 'release_date',
            
        }
    ))
    desc = forms.CharField(required=False, max_length=255, widget=forms.Textarea(
        attrs={
            'class': 'form-control ',
            'id': 'desc',
            'name': 'desc',
            'rows': 3,
        }
    ))