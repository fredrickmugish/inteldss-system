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

class Academic(models.Model):
    college = models.CharField(max_length=100)
    programs = models.CharField(max_length=100, null=True)
    enrollment_rate = models.IntegerField(null=True)
    
    class Meta:
        verbose_name = "Academic"
        verbose_name_plural = "Academic"
    
    def __str__(self):
        return self.college
    
class Facilities(models.Model):
    college = models.ForeignKey(Academic, on_delete=models.CASCADE, null=True)
    classrooms = models.CharField(max_length=100, null=True)
    library = models.CharField(max_length=100, null=True)
    laboratory = models.CharField(max_length=100, null=True)
    accomodation = models.CharField(max_length=100, null=True)
    playgrounds = models.CharField(max_length=100, null=True)
    online_resources = models.CharField(max_length=100, null=True)
    health_facilities = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name = "Facilities"
        verbose_name_plural = "Facilities"
    
class Finance(models.Model):
    college = models.ForeignKey(Academic, on_delete=models.CASCADE, related_name='college_finances', null=True)
    program = models.CharField(max_length=100)
    tuition_fee = models.CharField(max_length=100)
  
  
    class Meta:
        verbose_name = "Finance"
        verbose_name_plural = "Finance"

class Administrative(models.Model):
    policy = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Administrative"
        verbose_name_plural = "Administrative"

class Social(models.Model):
    sport = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Social"

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='documents/', max_length=255)

    def __str__(self):
        return self.title