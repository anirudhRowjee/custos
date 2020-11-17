from rest_framework.serializers import ModelSerializer
from .models import Item
from users import serializers


class ItemSerializer(ModelSerializer):

    user_list = serializers.ProfileSerializer(many=True)

    class Meta:
        model = Item
        fields = "__all__"
