from django.db import models

# Create your models here.
class Student(models.Model):
    studname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.studname
    
