from django import forms
from vendor.models import vendorRequest

class vendorRequestForm(forms.ModelForm):
    class Meta:
        model = vendorRequest
        exclude = ['status', "prepare_person", "approve_person", "State", "Country", "expiration_date"]
        widgets = {
            'vendor_address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'Note': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class vendorReviewForm(forms.ModelForm):
    class Meta:
        model = vendorRequest
        exclude = ['status']
        widgets = {
            'vendor_address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'Note': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class uploadAXvendors(forms.Form):
        excel_file = forms.FileField()