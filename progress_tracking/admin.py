from django.contrib import admin
from . import models

admin.site.register(models.Goal)
admin.site.register(models.ProgressUpdate)
