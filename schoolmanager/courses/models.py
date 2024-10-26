from django.db import models

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
    professor = models.CharField(max_length=30)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    