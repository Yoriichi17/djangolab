from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student 
from .models import Project #9
from .forms import CourseForm, StudentForm 
from .forms import ProjectForm #9
from django.views.generic import ListView, DetailView #10

def course_list(request):
    courses = Course.objects.all() 
    projects = Project.objects.all() #add this line for 9th program or no need
    return render(request, 'course_list.html', {'courses': courses , 'projects':projects}) #add 'projects':projects only for 9th 

def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    students = Student.objects.filter(course=course)
    return render(request, 'course_detail.html', {'course': course, 'students': students})

def register_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  
    else:
        form = CourseForm()
    return render(request, 'register_course.html', {'form': form})

def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})

def project_details(request, id): #9
    project = get_object_or_404(Project, id=id)
    students = Student.objects.filter(project=project)
    return render(request, 'project_detail.html', {'project': project, 'students': students})

def register_project(request): #9
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  
    else:
        form = ProjectForm()
    return render(request, 'register_project.html', {'form': form})





class StudentListView(ListView):#10
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):#10
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'
