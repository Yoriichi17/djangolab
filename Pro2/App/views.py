from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Student
from .forms import CourseForm, StudentForm

def course_list(request):
    courses = Course.objects.all() 
    return render(request, 'course_list.html', {'courses': courses})

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
