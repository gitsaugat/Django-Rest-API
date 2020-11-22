from django.db import models
from django.utils.timezone import datetime


class Assignment(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date_added = models.DateTimeField(default=datetime.utcnow())

    def __str__(self):
        return self.title


class Student(models.Model):
    fname = models.CharField(max_length=300)
    Lname = models.CharField(max_length=300)
    grade = models.IntegerField(max_length=12)
    admission_date = models.DateTimeField(auto_now_add=True)
    fatherName = models.CharField(max_length=300)
    mothersName = models.CharField(max_length=300)
    studentNumber = models.IntegerField(max_length=20)
    fathersNumber = models.IntegerField(max_length=20)
    mothersNumber = models.IntegerField(max_length=20)
    personalEmail = models.EmailField()
    schoolEmail = models.EmailField()

    def __str__(self):
        return f'{self.fname} {self.Lname}'
