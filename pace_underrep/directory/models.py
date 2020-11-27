from datetime import datetime

from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# switch this to just a string?
Visibility = ("PUBLIC", "AUTHED", "SHARED")


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Identity(Tag):

    class Meta:
        verbose_name_plural = 'Identities'
    pass


class Circuit(Tag):
    pass


class Involvement(Tag):
    pass


class DirUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,  **extra_fields):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None,  **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class DirUser(AbstractUser, models.Model):
    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(blank=True)
    propic = models.ImageField(blank=True)
    identities = models.ManyToManyField(Identity, blank=True)
    visibility = models.PositiveSmallIntegerField(default=Visibility.index("PUBLIC"), blank=True)
    circuits = models.ManyToManyField(Circuit, blank=True)
    involvements = models.ManyToManyField(Involvement, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # TODO: add location field

    @property
    def age(self):
        try:
            return int((datetime.now().date() - self.date_of_birth).days / 365.25)
        except TypeError:
            return 0

    @property
    def minor(self):
        return "Yes" if self.age < 18 else "No"

    @property
    def display_name(self):
        return self.first_name or self.email

    people = DirUserManager()

    def __str__(self):
        if self.last_name and self.first_name:
            return self.last_name + ", " + self.first_name
        else:
            return self.email

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = 'User'


class Definition(models.Model):
    word = models.CharField(max_length=50)
    definition = models.TextField()
