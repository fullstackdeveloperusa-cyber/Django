from django.contrib import admin
from .models import School
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display=['id', 'sno', 'sname', 'stype']
admin.site.register(School,SchoolAdmin)