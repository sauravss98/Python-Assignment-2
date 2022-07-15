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

class FishForm(forms.ModelForm):
    class Meta:
        model=ManageFish
        fields=['fishName','fishCount','fishSold']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=ManageDepartment
        fields=['departmentName','departmentCount']

class SalesForm(forms.ModelForm):
    class Meta:
        model=ManageSales
        fields=['fishSales','salesDate','fishName']

class CreditForm(forms.ModelForm):
    class Meta:
        model=ManageCredit
        fields=['creditYear','totalCredit']

