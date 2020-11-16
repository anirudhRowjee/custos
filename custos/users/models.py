from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from users import models as user_models

# Contains User Model Extension Layer (Profile) and Privilege Tables
class Profile(models.Model):
    """
    Base class for the User Profile
    """
    # one to one field to Django User model to extend it
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=100)

    def __str__(self):
        # string representation
        return f"{str(self.user)}"


# Signals - trigger certain functions when a new object is created
# create a new Profile Object when a user account is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# save the Profile object whenever the user model is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Privilege(models.Model):
    
    """ Privilege table - change who can do what on each list for each user """

    # defining privileges
    READER = "RD"
    EDITOR = "ED"
    OWNER = "OW"
    
    ROLE_CHOICES = [
        (READER, "READER"),
        (EDITOR, "EDITOR"),
        (OWNER, "OWNER")
    ]

    main_list = models.ForeignKey('lists.List', on_delete=models.CASCADE)
    user = models.ForeignKey(user_models.Profile, on_delete=models.CASCADE)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=OWNER)