from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'academic_class',
            'major',
            'gpa',
            'profile_pic',
        ]