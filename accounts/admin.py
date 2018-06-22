# admin.py
from django.contrib import admin  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  
from django.contrib.auth.models import Group
#from .models import Profile

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    
    list_display = (
                    'id', 'username', 'staffName',
                    'Department', 'DepManager', 'Title', 
                    'emailAddress', 'ManagerEmployee',
                    )
    list_filter = ('Department',)
    list_display_links = ['id', 'username', 'staffName']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': (
                                        'EmployeeID', 'staffName', 'Department', 
                                        'DepManager', 'Title', 'ManagerEmployee',
                                        'HiringDate', 'LeaveDate',
                                    )}),
        ('Permissions', {'fields': ('active', 'staff', 'admin',)}),
    )
    '''
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')})
        )
    '''
    search_fields = ('staffName',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.unregister(Group)  
admin.site.register(User, UserAdmin)  