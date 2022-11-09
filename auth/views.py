import json

from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from auth.serializer import UserSerializer


@api_view(["POST"])
# Create your views here.
def login(request):
    data = json.loads(request.body)

    user = authenticate(username=data["username"], password=data["password"])
    if user is None:
        return HttpResponse(status=401)

    django_login(request, user)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


def logout(request):
    django_logout(request)

    return HttpResponse(status=200)


def register(request):

    data = json.loads(request.body)

    user = User.objects.create_user(data["email"], data["email"], data["password"])
    user.first_name = data["firstName"]
    user.last_name = data["lastName"]
    user.save()

    return HttpResponse(status=200)


def csrf(request):
    token = get_token(request)

    return HttpResponse(token)
