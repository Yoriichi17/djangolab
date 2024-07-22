from django.urls import path
from .views import course_list, course_details, register_course, register_student, project_details, register_project
from .views import  project_details, register_project #9
from .views import StudentDetailView,StudentListView #10

urlpatterns = [
    path('course/', course_list, name='course_list'),
    path('course/<int:id>/', course_details, name='course_details'),
    path('course_reg/', register_course, name='register_course'),
    path('student_reg/', register_student, name='register_student'),
    path('project/<int:id>/', project_details, name='project_details'), #9
    path('project_reg/', register_project, name='register_project'), #9
    path('students/', StudentListView.as_view(), name='student_list'),#10
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),#10
]
