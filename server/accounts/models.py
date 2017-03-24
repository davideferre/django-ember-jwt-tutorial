"""Account model module."""
from __future__ import unicode_literals

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models
from django.utils.translation import ugettext as _
import uuid


class AppUserManager(BaseUserManager):
    """AppUser manager class."""

    def create_user(self, email, first_name, last_name, password=None):
        """Create and save a User with the given email, date of birth and password."""
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a superuser with the given email."""
        user = self.create_user(email, password=password, first_name=first_name, last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser):
    """AppUser model class (for customizing user model)."""

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name=_('E-mail address'), max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    timestamp_subscription = models.DateTimeField(auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now=True)

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Methods

    def get_full_name(self):
        """Return the user full name."""
        # The user is identified by their email address
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        """Return the user first name."""
        # The user is identified by their email address
        return self.first_name

    def __unicode__(self):
        """Unicode representation of the class."""
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        """String representation of the class."""
        return self.email

    def has_perm(self, perm, obj=None):
        """Do the user have a specific permission? Checking it."""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Do the user have permissions to view the app `Accounts`? Checking it."""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Checking if the user is a member of staff."""
        # Simplest possible answer: All admins are staff
        return self.is_admin
