from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model to handle creation of users and superusers.
    """
    def create_user(self, email, username, password=None, role='employee', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if role not in ['admin', 'manager', 'employee']:
            raise ValueError("Invalid role. Choose from 'admin', 'manager', or 'employee'.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with elevated permissions.
        """
        return self.create_user(email, username, password, role='admin', is_superuser=True, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model that uses email as the primary identifier for authentication.
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )

    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')  # Single role field
    is_active = models.BooleanField(default=True)  # Active status

    # Additional optional fields
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], blank=True, null=True)
    age = models.PositiveBigIntegerField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.email} ({self.role})"

    @property
    def is_staff(self):
        # Treat users with the 'admin' role as staff
        return self.role == 'admin'

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_manager(self):
        return self.role == 'manager'

    @property
    def is_employee(self):
        return self.role == 'employee'
