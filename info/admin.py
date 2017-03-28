from django.contrib import admin
from . import models


admin.site.register([models.Teacher, models.Cabinet, models.Lesson, models.Group])
