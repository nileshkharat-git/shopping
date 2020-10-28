from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        """"this function create simple user for an application"""
        if not email:
            raise ValueError('Email not provided')

        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password):
        """"this function create super(owner) user for an application"""
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

class Accounts(AbstractBaseUser):
    email = models.EmailField(max_length=255, primary_key=True,verbose_name="Email")
    username = models.CharField(max_length=255, verbose_name="Username")
    date_joined=models.DateField(auto_now_add=True)
    last_login=models.DateField(auto_now=True)

    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_supersuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    objects=MyManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    