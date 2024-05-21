from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','description','customer','created']
    list_filter  = ['title','description','customer','created']
    search_fields = ['title','description','customer','created']
