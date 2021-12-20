from django.db import models


# Create your models here.


class Semester(models.Model):
    semester = models.CharField(max_length=100)

    def __str__(self):
        return self.semester

class Subject(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.title+ " "+ self.code


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, unique=True)
    std_id = models.CharField(max_length=7)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name + " "+ self.std_id


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30, unique=True)
    semester = models.ManyToManyField(Semester)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name + " " + self.email


