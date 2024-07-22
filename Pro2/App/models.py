from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 100 )
    description = models.TextField()
    def __str__(self):
        return self.name
    
class Student(models.Model):
    f_name = models.CharField(max_length= 100)
    l_name = models.CharField(max_length= 100)
    email = models.EmailField()
    course = models.ManyToManyField(Course , related_name='students',blank=True)
    def __str__(self):
        return f"{self.f_name} {self.l_name}"