from django.db import models

# Create your models here.


class Student(models.Model):
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    student_mail = models.EmailField()
    student_marks = models.IntegerField()
    student_address = models.TextField()

    def __str__(self):
        return self.student_first_name + self.student_last_name


class Management(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=10)
    photo = models.ImageField(default="")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    testimonial_name = models.CharField(max_length=30)
    posted_on = models.DateField()
    testimonial_text = models.TextField()
    photo = models.ImageField(default="")
