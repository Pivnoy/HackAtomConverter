from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(max_length=100, blank=True)
    dir_path = models.TextField(max_length=100, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)
    instance.profile.save()
