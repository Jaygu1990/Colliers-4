from django import forms
from revrec.models import revrecmodel
class uploadrevrecform(forms.Form):
    excel_file = forms.FileField()