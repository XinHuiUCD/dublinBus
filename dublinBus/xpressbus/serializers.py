from rest_framework import serializers
from xpressbus.models.models import Stoprouteinfo

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stoprouteinfo
        fields = ('stopid', 'routesid', 'searchname', 'latitude', 'longitude')
