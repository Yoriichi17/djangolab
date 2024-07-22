from django import forms
from .models import Course, Student
from .models import Project #9

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']  

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['f_name', 'l_name', 'email', 'course','project']  # for 9th you need 'project' in the list or only keep first 3

class ProjectForm(forms.ModelForm):#9
    class Meta:
        model = Project
        fields = ['topic','lang','duration']
