from django.urls import path
from . import views  
urlpatterns = [
     path('riderinfo/', views.add_rider, name='add-items'),
     path('request/', views.add_request, name='add-request'), 
     path('myrequest/<int:reqid>/', views.get_requests, name='all-requests'),
     path('apply/<int:riderid>/', views.apply_rider, name='all-requests'),
     path('matchingrides/', views.matching_rides, name='all-requests'),
]