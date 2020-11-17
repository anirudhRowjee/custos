from django.db import models
from users import models as user_models

# signals - set the timestamp
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import datetime

# Contains models for Lists and Items in List


class Item(models.Model):

    """
    The Item is the core of the Application. A user can have multiple Items, and each item will have a time before which it will be considered
    unsafe. Once this time expires, the user will recieve a notification.

    A User can upload images to items. Users can also share items with other users, making sure they can view it, and that they will also be notified once it is safe to use/touch.
    """

    # this is the list of users that the items belongs to
    user_list = models.ManyToManyField(to=user_models.Profile)

    # the name of the item
    name = models.CharField(max_length=100)

    # added timestamp
    created = models.DateTimeField(auto_now_add=True)

    # seconds of delta to when it's safe
    delta = models.BigIntegerField(default=0)

    # expected time by which it'll be safe
    expected_elapsed_timestamp = models.DateTimeField(blank=True, null=True)

    # boolean flag to skip computation, perhaps run a cron job to check all items on routine
    safe = models.BooleanField(default=False)

    def __str__(self):
        # string representation
        return f"{self.name} - {str(self.user_list)}"


@receiver(post_save, sender=Item)
def set_delta_callback(sender, instance, **kwargs):

    print("Entering Signal")

    if not instance.expected_elapsed_timestamp:

        # at this point, perform the addition and save the item as an instance of datetime.datetime
        time_of_creation = instance.created

        # delta in seconds
        delta = instance.delta

        # add the time delta from the timedelta object - this, somehow, works
        delta = datetime.timedelta(seconds=delta)

        time_of_expiry = time_of_creation + delta

        # just PRAY this works
        instance.expected_elapsed_timestamp = time_of_expiry
        instance.save()
