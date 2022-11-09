import json

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from places.serializers import PlaceSerializer
from django.contrib.gis.geos import Point
from django.views.decorators.csrf import csrf_exempt

from places.models import Place


@api_view(["GET"])
# Create your views here.
def index(request):

    if request.user.is_anonymous:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    places = Place.objects.filter(user_id=request.user.id).order_by("created").all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


@api_view(["POST"])
# Create a new place for a user
def create(request):

    if request.user.is_anonymous:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    place = Place()
    place.user = request.user
    place.name = request.data["name"]
    place.created = timezone.now()

    place.location = Point(request.data["longitude"], request.data["latitude"])
    place.save()

    return Response(place.id, status=status.HTTP_200_OK)


@api_view(["DELETE"])
# Delete a place for a user
def delete(request, place_id):

    if request.user.is_anonymous:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    place = Place.objects.get(id=place_id, user_id=request.user.id)
    place.delete()

    return Response(status=status.HTTP_200_OK)
