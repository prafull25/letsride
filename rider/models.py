
import enum
from django.db import models

class travelMediumsTypes(enum.Enum):
  Bus="BUS"
  Car="CAR"
  Train="TRAIN"
  @classmethod
  def choices(cls):
    return tuple((i.name, i.value) for i in cls)
    

class assetTypeChoice(enum.Enum):
  LAPTOP="LAPTOP"
  TRAVEL_BAG="TRAVEL_BAG"
  PACKAGE="PACKAGE"
  @classmethod
  def choices(cls):
    return tuple((i.name, i.value) for i in cls)


class assetSensitivityChoice(enum.Enum):
  HIGHLY_SENSITIVE="HIGHLY_SENSITIVE"
  SENSITIVE="SENSITIVE"
  NORMAL="NORMAL"
  @classmethod
  def choices(cls):
    return tuple((i.name, i.value) for i in cls)


class  statusChoice(enum.Enum):
   Pending= "Pending"
   Expired="Expired"
   @classmethod
   def choices(cls):
    return tuple((i.name, i.value) for i in cls)
   

class Rider(models.Model):
    id = models.AutoField(primary_key=True)
    fromLocation = models.CharField(max_length=255)
    toLocation = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    assetQuantity=models.PositiveIntegerField()
    isApplied= models.BooleanField(default=False)
    travelMedium = models.CharField(max_length=50,choices=travelMediumsTypes.choices())


class Requester(models.Model):
    id = models.AutoField(primary_key=True)
    reqid = models.CharField(max_length=3,default="1")
    fromLocation = models.CharField(max_length=255)
    toLocation = models.CharField(max_length=255)
    dateTime = models.DateTimeField()
    assetQuantity=models.PositiveIntegerField()
    assetType=models.CharField(max_length=50,choices=assetTypeChoice.choices())
    assetSensitivity=models.CharField(max_length=50,choices=assetSensitivityChoice.choices())
    whomToDeliver= models.CharField(max_length=255,default="")
    status=models.CharField(max_length=50,choices=statusChoice.choices(),default="Pending")  