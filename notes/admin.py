from django.contrib import admin
from django.db import models
from django.contrib import admin
from . import models





class NotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Notes, NotesAdmin)