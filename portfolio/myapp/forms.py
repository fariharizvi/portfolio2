from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'contactno', 'branch', 'photo']  # fields to show in form

def clean_contactno(self):
        contact = self.cleaned_data.get('contactno')
        if contact and not contact.isdigit():
            raise forms.ValidationError("Contact number must contain digits only.")
        return contact

