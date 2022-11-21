from time import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from project.settings import MEDIA_URL, STATIC_URL


# Create your models here.

class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Tienes que proporcionar un email válido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email,password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email,password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    CHOICE_ROL=[
        ('S','Supervisor de Calidad'),
        ('D','Desarrollador'),
        ('I','Diseñador'),
        ('A','Analista'),
    ]
    
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True,default='avatar/avatar.svg')
    #CHOICE_ROL | S= Supervisor de Calidad, D= Desarrollador , I= Diseñador , A= Analista
    rol=models.CharField(max_length=1, choices=CHOICE_ROL, default='D')

    objects = CustomUserManager()

    USERNAME_FIELD= 'email'
    EMAIL_FIELD= 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_avatar(self):
        if self.avatar:
            return '{}{}'.format(MEDIA_URL, self.avatar)
        return '{}{}'.format(STATIC_URL, 'avatar/avatar.svg')