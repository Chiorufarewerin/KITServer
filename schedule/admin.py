from django.contrib import admin

from schedule import models

admin.site.register([models.TeachLesson, models.DaySchedule, models.GroupSchedule])
