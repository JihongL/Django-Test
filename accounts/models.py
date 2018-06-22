# models.py
from django.db import models  
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save  
from django.dispatch import receiver
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    objects = UserManager()
    username = models.CharField(verbose_name="User ID", max_length=50, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


    EmployeeID = models.CharField(verbose_name="사번", max_length=10, blank=True, null=True, unique=True)
    
    staffName = models.CharField(
        u'이름', 
        max_length=10, 
        blank=False,
        default='')
    emailAddress = models.EmailField(verbose_name='Email', max_length=50, blank=True, null=True, editable=False)
    def save(self, *args, **kwargs):
        self.emailAddress = '{}@bespinglobal.com'.format(self.username)
        super().save()
        return
    dep_CHOICES = (
    ('Azure', 'Azure'),
    ('AWS', 'Amazon Cloud Service'), 
    ('PM', 'Project Manager'),
    ('PMO', 'Project Manager Operation'),
    ('CDP', 'Cloud Data '),
    )
    Department = models.CharField(max_length=50, null=True, blank=True, choices=dep_CHOICES)
    DepManager = models.BooleanField(default=False)

    title_CHOICES = (
    ('기타', '기타'),
    ('사원', '사원'),
    ('대리', '대리'),
    ('과장', '과장'),
    ('차장', '차장'),
    ('부장', '부장'),
    ('이사', '이사'),
    ('위원', '위원'),
    ('상무', '상무'),
    )
    Title = models.CharField(max_length=5, choices=title_CHOICES, null=True)

    HiringDate = models.DateField(default=timezone.now)
    LeaveDate = models.DateField(blank=True, null=True)
    ManagerEmployee = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active
    

    def __str__(self):
        return '{} {}'.format(self.Department, self.staffName)

'''
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
'''