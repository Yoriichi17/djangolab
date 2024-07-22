from django.urls import path
from .views import course_list, course_details, register_course, register_student, project_details, register_project

urlpatterns = [
    path('course/', course_list, name='course_list'),
    path('course/<int:id>/', course_details, name='course_details'),
    path('course_reg/', register_course, name='register_course'),
    path('student_reg/', register_student, name='register_student'),
    path('project/<int:id>/', project_details, name='project_details'),  # Correct URL pattern for project_details
    path('project_reg/', register_project, name='register_project'),
]
