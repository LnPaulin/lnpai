from .models import *
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ProfileForm(forms.ModelForm):
    address = forms.CharField(
        required=True,
        label='Address ',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address'}))
    city = forms.CharField(
        required=True,
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your City'}))
    region = forms.CharField(
        required=True,
        label='Region',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your Region'}))
    country =  forms.CharField(
        required=True,
        label='Country',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your Country'}))
    postalCode = forms.CharField(
        required=True,
        label='Postal Code',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Your Postal code'}))

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
        Row(Column('address',css_class='form-group col-md-6'),Column('city',css_class='form-group col-md-6')),
        Row(Column('region',css_class='form-group col-md-6'),Column('country',css_class='form-group col-md-6')),
        Row(Column('postalCode',css_class='form-group col-md-6')),
        Submit('submit', 'Save Changes', css_class="btn-primary me-2")
         )

class Meta:
    model=Profile
    fields=['address','city','region','country','postalCode']

    