
from django.db import models
from django.contrib.auth.models import User

from website.models import Department


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=300,null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField( null=True, blank=True)
    phone = models.CharField(max_length=30,  null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username

class Appoinment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    date = models.DateField()
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name