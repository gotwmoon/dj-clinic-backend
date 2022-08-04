

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    director = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'department/', default='department/default.jpg') 
    created_date = models.DateTimeField(auto_now_add=True)
    #is_staff

    def __str__(self):
        return self.title


class Service(models.Model):
    owner = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




WEEKDAYS = [
  (1, ("Monday")),
  (2, ("Tuesday")),
  (3, ("Wednesday")),
  (4, ("Thursday")),
  (5, ("Friday")),
  (6, ("Saturday")),
  (7, ("Sunday")),
]

class TimeSchedule(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        return "{}:  {} - {}".format(self.get_weekday_display(), self.from_hour, self.to_hour)    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)        
    updated_date = models.DateTimeField(auto_now=True)        

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email       