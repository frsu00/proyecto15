from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=100)
    dummydata = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, through='Enrollment')

    def __str__(self):
        return self.name


class Teach(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    def __str__(self):
        return self.course.name + ' ' + self.teacher.user.username


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        return self.course.name + ' ' + self.student.user.username
