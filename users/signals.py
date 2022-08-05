from django.db.models.signals import post_save, post_delete
from .models import User, Patient

def create_profile(sender, instance, created, **kwargs):

    if created:
        user = instance
        profile = Patient.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

post_save.connect(create_profile, sender=User)        