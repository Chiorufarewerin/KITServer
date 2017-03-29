from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from schedule.models import GroupSchedule
import json


def getschedule(request):
    return HttpResponse(json.dumps([i.as_json() for i in GroupSchedule.objects.all()],ensure_ascii=False))
