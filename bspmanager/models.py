from django.db import models
import uuid
# Create your models here.
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from random import randint
from datetime import date
from django.conf import settings
User = settings.AUTH_USER_MODEL
 
class TaskMaster(models.Model): 
    
    task_CHOICES = (
    ('PRE', 'Presales'),
    ('PJT', 'Project'),
    ('OTH', 'Others'),
    )
    TaskCategory = models.CharField(max_length=50, choices=task_CHOICES)

    TaskName = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()
    TaskOwner = models.ForeignKey(User, on_delete=models.CASCADE)

    dep_CHOICES = (
    ('Azure', 'Azure'),
    ('AWS', 'Amazon Cloud Service'),
    ('PM', 'Project Manager'),
    ('PMO', 'Project Manager Operation'),
    ('CDP', 'Cloud Data '),
    )
    SalesDepartment = models.CharField(max_length=50, null=True, blank=True, choices=dep_CHOICES)

    SalesRepresentative = models.CharField(max_length=50, blank=True, null=True)
    Remarks = models.TextField(blank=True, null=True)
    ModifiedDate = models.DateTimeField(auto_now_add=True)
    
    TaskID = models.EmailField(verbose_name='Task ID', max_length=50, blank=True, null=True, editable=False)
    def save(self, *args, **kwargs):
        self.TaskID = '{}-{}-{}'.format(self.TaskCategory, date.today().year, uuid.uuid4().hex[:5]) 
        super().save()
        return

    def __str__(self):
        return self.TaskName

    def display_detail(self):
        return ', '.join([self.TaskCategory, self.TaskDESC])
    display_detail.short_description = 'Detail'
 

class ResourceAllocation(models.Model):
    EmployeeName = models.ForeignKey(User, on_delete=models.CASCADE)
    TaskName = models.ForeignKey(TaskMaster, on_delete=models.CASCADE)
    TaskID = models.CharField(max_length=50, blank=True, null=True, editable=False)
    StartDate = models.DateField()
    EndDate = models.DateField()
    emailAddress = models.EmailField(max_length=50, blank=True, null=True, editable=False)
    TaskDESC = models.TextField(blank=True, null=True)
    def Status(self):
        if date.today() > self.EndDate:
            return "Finished"
        else:
            return "Active"
    def save(self, *args, **kwargs):
        self.emailAddress = '{}@bespinglobal.com'.format(self.EmployeeName.username)
        self.TaskID = self.TaskName.TaskID
        super().save()
        return
'''
class weeklyRM(models.Model):

    workHour = models.IntegerField(default=40)
    def dep(self):

'''