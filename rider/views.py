import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rider, Requester
from .serializers import RiderSerializer,RequesterSerializer
from rest_framework import serializers
from rest_framework import status
from django.core.paginator import Paginator
  

@api_view(['POST'])
def add_rider(request):
    rider = RiderSerializer(data=request.data)
    if rider.is_valid():
        rider.save()
        return Response(rider.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_request(request):
    requester = RequesterSerializer(data=request.data)
    if requester.is_valid():
        requester.save()
        return Response(requester.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_requests(request,reqid):
    data=Requester.objects.filter(dateTime__lt=datetime.datetime.now())
    for req in data:
        req.status="Expired"
        req.save()   
    requests=Requester.objects.filter(reqid=reqid)
    if request.data['statusFilter']!="":
        requests=requests.filter(status=request.data['statusFilter'])
    if request.data['assetFilter']!="":
        requests=requests.filter(status=request.data['assetFilter'])
    if request.data['sort']:
        requests=requests.order_by("dateTime").values()
    pages = Paginator(requests,request.data['pagesize']) 
    page_obj = pages.page(request.data['pageno'])
    return Response(page_obj.object_list)

@api_view(['PUT'])
def apply_rider(request,riderid):
    rider=Rider.objects.get(id=riderid)
    rider.isApplied=True
    rider.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def matching_rides(request):
    riders=Rider.objects.filter(fromLocation=request.data["fromLocation"], toLocation=request.data["toLocation"],dateTime=request.data["dateTime"]).values()
    return Response(riders)
