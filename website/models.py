from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    class Meta:
        verbose_name = "organization"
        verbose_name_plural = "organization"

class Disruptor(models.Model):
    category = models.CharField(max_length=200)
    affected_aspect = models.CharField(max_length=200)
    class Meta:
        verbose_name = "disruptor"
        verbose_name_plural = "disruptors"

class Team(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')
    class Meta:
        verbose_name = "Team Members"
        verbose_name_plural = "Team Members"

class Student(models.Model):
    regNo = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Students"
        verbose_name_plural = "Students"

class Employees(models.Model):
    empId = models.CharField(max_length=100)
    fName = models.CharField(max_length=100)
    sName = models.CharField(max_length=100)
    lName = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    orgName = models.CharField(max_length=100)
    professional = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"

