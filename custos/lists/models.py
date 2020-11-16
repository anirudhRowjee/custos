from django.db import models
from users import models as user_models

# Contains models for Lists and Items in List

class List(models.Model):
    """
    List Item - Users will be able to add objects to this,
    and can maintain different lists for different things (eg grocery, amazon, deliveries, etc)
    """

    # the user the list is bound to
    user = models.ForeignKey(user_models.Profile, on_delete = models.CASCADE)

    # the name of the list
    name = models.CharField(max_length=100)

    # created timestamp
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        # string rep
        return f"{self.name} ({self.user})"


class Item(models.Model):
    """
    Item - Users will be able to add items to a list, and the time it came in on, as well as the expected
    expiry time, such as 24 hours, 48 hours, 30 mins, etc
    One item can be added to one list.
    """

    # the list that the item is bound to
    user_list = models.ForeignKey(List, on_delete=models.CASCADE)

    # the name of the item
    name = models.CharField(max_length=100)

    # added timestamp
    created = models.DateField(auto_now_add=True)

    # expected time by which it'll be safe
    expected_elapsed_timestamp = models.DateTimeField()

    # boolean flag to skip computation, perhaps run a cron job to check all items on routine
    safe = models.BooleanField(default=False)

    def __str__(self):
        # string representation
        return f"{self.user_list.name} - {self.name}"
