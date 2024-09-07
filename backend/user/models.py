from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# class User(AbstractUser):
#     code = models.CharField(
#         verbose_name='code',
#         max_length=100,
#         unique=True
#     )
#     username = models.CharField(null=True, blank=True, max_length=100)
#     is_superuser = models.BooleanField(default=True)
#
#     def __str__(self):
#         return f"Store {self.id}: {self.code}"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user manager to deal with users where the code is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, code, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not code:
            raise ValueError('The Code field must be set')
        user = self.model(code=code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, code, password=None, **extra_fields):
        """
        Create and return a superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(code, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model where the 'code' is the unique identifier for authentication.
    """
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'code'  # Use 'code' instead of 'username'
    REQUIRED_FIELDS = []  # No additional fields are required

    def __str__(self):
        return self.code
