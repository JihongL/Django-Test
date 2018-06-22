from django.contrib import admin
from .models import TaskMaster, ResourceAllocation

# Register your models here.

@admin.register(TaskMaster)
class TaskMasterAdmin(admin.ModelAdmin):
    list_display = ('TaskID', 'TaskName', 'TaskCategory', 'StartDate', 'Remarks')
    list_filter = ('TaskCategory',)

@admin.register(ResourceAllocation)
class ResourceAllocationAdmin(admin.ModelAdmin):
    list_display = ('TaskID', 'TaskName', 'EmployeeName', 'StartDate', 'EndDate', 'Status', )
