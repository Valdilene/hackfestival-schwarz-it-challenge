from rest_framework import serializers

from .models import UpCycleRequest
from item.serializers import ItemSerializer

from user.serializers import UserSerializer

from item.models import Item


class UpCycleRequestSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = UpCycleRequest
        fields = ['id', 'requestsAt', 'store', 'items', 'user']

    def create(self, validated_data):
        items = validated_data.pop('items')
        upCycleRequest = UpCycleRequest.objects.create(**validated_data)

        for item in items:
            Item.objects.create(upCycleRequest=upCycleRequest, **item)
        return UpCycleRequest
