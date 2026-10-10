from django import forms
from .models import Student2, Address2

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'address']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),       }
            
        
