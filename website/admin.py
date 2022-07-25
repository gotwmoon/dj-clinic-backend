from django.contrib import admin
from .models import Department, Service, TimeSchedule, Contact

admin.site.register(Department)
admin.site.register(Service)
admin.site.register(TimeSchedule)
admin.site.register(Contact)


