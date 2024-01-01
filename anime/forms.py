# di file forms.py
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, label='Cari Anime')
