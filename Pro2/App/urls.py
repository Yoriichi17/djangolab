from django.urls import path
from .views import course_list, course_details, register_course, register_student

urlpatterns = [
    path('course/', course_list, name='course_list'),
    path('course/<int:id>/', course_details, name='course_details'),  # This name should be 'course_details'
    path('course_reg/', register_course, name='register_course'),
    path('student_reg/', register_student, name='register_student'),
]
