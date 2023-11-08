from django import forms
from .models import students
from django.forms import ModelForm, TextInput, DateInput, EmailInput

 
class studentform(forms.ModelForm):
    class Meta:
        model = students
        fields = '__all__'

        widgets={
            'student_number': forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter Student Number'}) , 
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter First Name'}) , 
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter Last Name'}) , 
            'gender': forms.Select(attrs={'class': 'form-control', 'style': 'max-width: 500px;'}) ,
            'date_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'style': 'max-width: 500px;'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter Phone Number'}) , 
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter email address'}) , 
            'address': forms.TextInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter address'}) , 
            'cgpa':forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width: 500px;', 'placeholder': 'Enter CGPA'}) , 

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""