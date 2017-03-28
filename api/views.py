from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from chedule.models import GroupChedule
import json


def getschedule(request):
    return HttpResponse(json.dumps([i.as_json() for i in GroupChedule.objects.all()],ensure_ascii=False))
