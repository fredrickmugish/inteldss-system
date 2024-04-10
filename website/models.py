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