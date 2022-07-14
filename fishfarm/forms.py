from .models import *
from django import forms

class DamForm(forms.ModelForm):
    class Meta:
        model=ManageDam
        fields=['damName','damLocation','damHeight']

class StaffForm(forms.ModelForm):
    class Meta:
        model=ManageStaff
        fields=['staffid','staffname','staffEmail','staffImage']