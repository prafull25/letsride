from django.db.models import fields
from rest_framework import serializers
from .models import Rider,Requester
  
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('id','fromLocation', 'toLocation', 'dateTime', 'assetQuantity','isApplied','travelMedium')

class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        fields = ('id','reqid','fromLocation', 'toLocation', 'dateTime', 'assetQuantity','assetType','assetSensitivity','whomToDeliver','status')