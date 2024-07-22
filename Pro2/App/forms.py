from django import forms
from .models import Course, Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']  

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['f_name', 'l_name', 'email', 'course']  
