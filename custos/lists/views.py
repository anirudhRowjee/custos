from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse
from django.contrib.auth.models import User

from . import models as list_models
from .serializers import ItemSerializer
from users import models as user_models


def itemsview(request):
    # getting the logged in user
    user = request.user
    if user is None:
        return render(request, "users/login.html")
    return render(request, "lists/lists.html")


# API View Section
def items(request, id):
    if request.method == "GET":
        print(request.POST)
        # serialize all the items that the user owns
        uid = request.user.id
        if not uid:
            return JsonResponse(
                {"error": 400, "message": "Please Login to Access this Data"}
            )

        user = User.objects.get(id=uid)

        if not user:
            return JsonResponse({"error": 400, "message": "user does not exist"})

        print("User object found", user)

        profile_object = user_models.Profile.objects.get(user=user)
        print("Profile object found", profile_object)

        # filter items to get only those which have the user
        items = list_models.Item.objects.all().filter(
            user_list__id=int(profile_object.id)
        )
        print("Item list found")

        serialized = ItemSerializer(items, many=True).data
        print("Item list serialized")

        print(serialized)
        return JsonResponse(serialized, safe=False)

    elif request.method == "POST":
        """
        Expected Parameters -
        Request Body
        1. Name (text)
        2. Time Period Necessary (seconds)
        3. Image? (Maybe)
        """
        # make a new item

        data = request.POST
        print(request)

        # data cleaning
        try:
            name = data.get("name")
            time_delta = data.get("time")
            user_id = data.get('user_id')
            print(name, time_delta, user_id)   
        except MultiValueDictKeyError:
            # return JSON request - something wrong
            return JsonResponse({"status": 400, "error": "Incomplete Request Body"})

        # making the new objects
        new_item = list_models.Item(name=name, delta=time_delta)

        # user profile to add to the list
        user_object = User.objects.get(id = user_id)
        profile = user_models.Profile.objects.all().filter(user__id = user_id)[0]
        new_item.user_list.add(profile)

        # this calls the signal which makes the timestamp delta work
        new_item.save()

    elif request.method == "PUT":
        # update the current item
        pass

    elif request.method == "DELETE":
        # delete the current item
        pass
