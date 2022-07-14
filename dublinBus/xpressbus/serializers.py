from rest_framework import serializers
from .models import Bus

class BusSerializer(serializers.HyperlinkedModelSerialzer):
    class Meta:
        model = Bus
        fields = ('routeId', 'lat', 'lon')
