
from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=300,null=True, blank=True)
    username= models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    birthday = models.DateField()
    phone = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username

