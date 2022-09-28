from tkinter import CASCADE
from django.db import models

# Create your models here.



class Student(models.Model):

    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    national_id = models.CharField(max_length=15)
    city_name= models.ForeignKey('City', on_delete=models.CASCADE)
    course_name= models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Course(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name