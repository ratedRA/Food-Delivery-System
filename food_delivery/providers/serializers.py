from rest_framework import serializers
from .models import Restaurants, Delivery_partners


class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ['res_name', 'x', 'y']

class DelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_partners
        fields = ['name', 'x', 'y']