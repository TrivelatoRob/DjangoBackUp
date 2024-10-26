from django.db import models
<<<<<<< HEAD
from courses.models import Courses


# Create your models here.

    
=======

# Create your models here.

class Courses(models.Model):
    COURSE_CHOICES = [
        ('matematica', 'Matemática'),
        ('portugues', 'Português'),
        ('historia', 'História'),
        ('geografia', 'Geografia'),
        ('ciencias', 'Ciências'),
        ('ingles', 'Inglês'),
        ('ed_fisica', 'Educação Física'),
        ('artes', 'Artes'),
        ('literatura', 'Literatura'),
        ('quimica', 'Química'),
        ('fisica', 'Física'),
        ('biologia', 'Biologia'),
    ]
    name = models.CharField(max_length=30, choices=COURSE_CHOICES)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

>>>>>>> 60e98359149ab120318e7fd4b05bb06d4502b5cb
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(Courses, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.enrollment_date}"
