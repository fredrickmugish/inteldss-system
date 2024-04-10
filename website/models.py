from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "organization"
        verbose_name_plural = "organization"

class Disruptor(models.Model):
    category = models.CharField(max_length=200)
    affected_aspect = models.CharField(max_length=200)
    def __str__(self):
        return self.affected_aspect
    class Meta:
        verbose_name = "disruptor"
        verbose_name_plural = "disruptor"

class Team(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Team Members"
        verbose_name_plural = "Team Members"