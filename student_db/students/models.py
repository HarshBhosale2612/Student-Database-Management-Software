from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField(unique=True,null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    marks = models.FloatField(null=True, blank=True)
    attendance = models.FloatField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"