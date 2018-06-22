from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
#from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.db.models import Q
from accounts.models import User

from .models import TaskMaster, ResourceAllocation
from django.conf import settings
from django.contrib.auth import get_user_model

import datetime
from datetime import date

def index(request):

    if request.user.id:
        email = User.objects.filter(username=request.user.username)[0].emailAddress
        manager = User.objects.filter(username=request.user.username)[0].DepManager
            
        if manager == False:
            fromDate = request.GET.get('fromDate', '')
            if fromDate:
                fromDate = datetime.date(int(fromDate[:4]), int(fromDate[5:7]), int(fromDate[8:10]))
            else:
                fromDate = datetime.date(2010, 1, 1)
        
            toDate = request.GET.get('toDate', '')
            if toDate:
                toDate = datetime.date(int(toDate[:4]), int(toDate[5:7]), int(toDate[8:10])) + datetime.timedelta(days=1)
            else:
                toDate = datetime.date(2999, 12, 31)
        
            q = request.GET.get('q', '') 
            if q:
                services = ResourceAllocation.objects.filter(
                            Q(TaskName__icontains=q) & Q(StartDate__range=[fromDate, toDate]) & Q(emailAddress=email)).order_by('-StartDate')
            else:
                services = ResourceAllocation.objects.filter(
                        Q(StartDate__range=[fromDate, toDate]) & Q(emailAddress=email)).order_by('-StartDate')
            count = services.count()
            context = {'services': services,
                        'q': q,
                        'count':count}
        
            return render(request, 'bspmanager/index.html', context)
        
        elif manager == True:
            fromDate = request.GET.get('fromDate', '') 
            if fromDate:
                fromDate = datetime.date(int(fromDate[:4]), int(fromDate[5:7]), int(fromDate[8:10]))
            else:
                fromDate = datetime.date(2010, 1, 1)
        
            toDate = request.GET.get('toDate', '')
            if toDate:
                toDate = datetime.date(int(toDate[:4]), int(toDate[5:7]), int(toDate[8:10])) + datetime.timedelta(days=1)
            else:
                toDate = datetime.date(2999, 12, 31)
        
            q = request.GET.get('q', '')
            if q:
                services = ResourceAllocation.objects.filter(
                        Q(TaskName__icontains=q) & Q(StartDate__range=[fromDate, toDate])).order_by('-StartDate')
            else:
                services = ResourceAllocation.objects.filter(
                        Q(StartDate__range=[fromDate, toDate])).order_by('-StartDate')

            count = services.count()
            context = {'services': services,
                        'q': q,
                        'count':count}

            return render(request, 'bspmanager/index.html', context)
            
    else:
        return redirect('login')
    

def scheduleindex(request):
    if request.user.id:
        
        fromDate = request.GET.get('fromDate', '')
        if fromDate:
            fromDate = datetime.date(int(fromDate[:4]), int(fromDate[5:7]), int(fromDate[8:10]))
        else:
            fromDate = datetime.date(2010, 1, 1)
    
        toDate = request.GET.get('toDate', '')
        if toDate:
            toDate = datetime.date(int(toDate[:4]), int(toDate[5:7]), int(toDate[8:10])) + datetime.timedelta(days=1)
        else:
            toDate = datetime.date(2999, 12, 31)
        
        #q = request.GET.get('q', '')
        
        dept_name = request.GET.get('Department','')
        
        EmployeeName = request.GET.get('staffName','')
        
        status1 = request.GET.get("status1","nav-item active")
        status2 = request.GET.get("status2","nav-item")
        status3 = request.GET.get("status3","container tab-pane active")
        status4 = request.GET.get("status4","container tab-pane")

        manager = User.objects.filter(username=request.user.username)[0].DepManager

        dept = User.objects.filter(username=request.user.username)[0].Department
        
        if manager == False:
            
            emp_Email = User.objects.filter(username=request.user.username)[0].emailAddress  
            services = ResourceAllocation.objects.filter(Q(StartDate__range=[fromDate, toDate]) &
                                                Q(emailAddress=emp_Email))
        
        elif manager == True:
            services = ResourceAllocation.objects.filter(Q(StartDate__range=[fromDate, toDate]) &
                                                    Q(Department__contains=dept))
            
        #if q:
            
           # services = services.filter(TaskName__contains=q)
        
        if dept_name:
            
            services = services.filter(Department__contains=dept_name)
            
        if EmployeeName:
            
            services = services.filter(contains=EmployeeName)
        
        servicesY = services.filter(Q(EndDate__lte=date.today())).order_by('-StartDate')
        services = services.filter(Q(EndDate__gte=date.today())).order_by('StartDate')

        count = services.count()
        countY = servicesY.count()
        
        context = {'services': services,
                   'servicesY':servicesY,
                   'count':count,
                   'countY':countY,
                   'dept':dept,
                   'manager':manager,
                   'status1':status1,
                   'status2':status2,
                   'status3':status3,
                   'status4':status4}
        
        return render(request, 'bspmanager/scheduleindex.html', context)

    else:
        return redirect('login')