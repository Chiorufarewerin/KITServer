from django.contrib import admin

from chedule import models

admin.site.register([models.TeachLesson, models.DayChedule, models.GroupChedule])
