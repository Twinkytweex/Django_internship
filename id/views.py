from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict


def json(request):
    data = list(Id.objects.values())

    return JsonResponse(data, safe=False)
