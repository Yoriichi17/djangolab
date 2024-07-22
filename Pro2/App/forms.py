from django import forms
from .models import Course, Student,Project

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']  

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['f_name', 'l_name', 'email', 'course','project']  

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic','lang','duration']
