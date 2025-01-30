from dataclasses import field

from autoslug.utils import slugify
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required for Employees')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class AbstractClinicalEmployee(AbstractUser):
    objects = EmployeeManager()  # Убедитесь, что EmployeeManager определён корректно
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "Clinical Employee"
        verbose_name_plural = "Clinical Employees"

    class EmployeeType(models.TextChoices):
        SELECT = 'Click to select', 'Click to select'
        DOCTOR = 'DR', 'Doctor'
        RECEPTION = 'RECEPTION', 'Reception'

    class GenderClinicalEmployee(models.TextChoices):
        SELECT = 'Click to select', 'Click to select'
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='clinicalemployee_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='clinicalemployee_permissions_set',
        blank=True
    )


    contact_number = models.CharField(
        max_length=15,
        blank=True,
        null=False
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    employee_type = models.CharField(
        max_length=50,
        choices=EmployeeType.choices,
        default=EmployeeType.SELECT
    )

    gender_employee = models.CharField(
        max_length=50,
        choices=GenderClinicalEmployee.choices,
        default=GenderClinicalEmployee.SELECT
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_type})"


class DRClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "DR"
        verbose_name_plural = "DR's"

    class DrSpecialityType(models.TextChoices):
        select_speciality = 'Click to select', 'Click to select'
        dermotology = 'DERMOTOLOGY', 'DERMOTOLOGY'
        plastic_surgery = 'PLASTIC SURGERY', 'PLASTIC SURGERY'
        aesthetic_medicine_dermatologist = 'Aesthetic Medicine Dermatologist', 'Aesthetic Medicine Dermatologist'


    medical_order_ID = models.CharField(
        _("Medical Order ID"),
        unique=True,
        null=False,
        help_text=_("A unique identifier for the medical order assigned to this user. This ID is used to track the user's medical orders.")
    )

    speciality_type = models.CharField(
        max_length=50,
        choices=DrSpecialityType.choices,
        default='Click to select'
    )

    def __str__(self):
        return f"Dr {self.first_name} {self.last_name} {self.medical_order_ID}"


class ReceptionsClinicalEmployee(AbstractClinicalEmployee):
    class Meta:
        verbose_name = "Reception Assistant"
        verbose_name_plural = "Reception's Assistant"

    def __str__(self):
        return f"(Reception) {self.first_name} {self.last_name}"