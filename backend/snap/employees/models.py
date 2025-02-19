from dataclasses import field
from autoslug.utils import slugify
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.utils.translation import gettext as _




#TODO AO CRIAR UM NOVO REGISTO DEVE SER PEDIDO U NOME DE RESPONSAVEL DE CLINICA COM OS DADOS TODOS
#É IMPORTANTISSIMO QUE O REGISTO SEJA FEITO POR UM RESPONSAVEL DE CLINICA
#É IMPORTANTE QUE O REGISTO SEJA FEITO POR UM RESPONSAVEL DE CLINICA


'''class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)
'''
#Employees accounts
#Abstract employee model
class BasicCustomEmployee(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='%(app_label)s_%(class)s_groups',  # Unique related name
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='%(app_label)s_%(class)s_permissions',  # Unique related name
        blank=True
    )

    class Rules(models.TextChoices):
        sl = 'Click to select', 'Click to select'
        dr = 'Doctor', 'Doctor'
        rc = 'Receptionist', 'Receptionist'
        it = 'It Dev', 'It Dev'

    class Gender(models.TextChoices):
        SELECT = 'Click to select', 'Click to select'
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'

    username = models.CharField(
        null=True,
        blank=False,
        unique=False
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, null=True, blank=False)
    gender= models.CharField(max_length=20, choices=Gender.choices, default=Gender.SELECT)  
    role= models.CharField(max_length=20, choices=Rules.choices, default=Rules.sl)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# Single receptionist User Model 
class ReceptionsClinicalEmployee(BasicCustomEmployee):
    class Meta:
        verbose_name = _('receptionist')
        verbose_name_plural = _('receptionists')

# Single Doctor User Model
class DrClinicalEmployee(BasicCustomEmployee):
    class Meta:
        verbose_name = _('Dr')
        verbose_name_plural = _('Dr\'s')

    medical_order_id = models.CharField(max_length=50, unique=True)
    specialty_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


#Buisnes accounts
# Custom User Model(ofice with single dr(user))
class SingleCustomUser(DrClinicalEmployee):
    class UserTypeChouse(models.TextChoices):
        SINGLE = 'single', 'Single User'
        HOSPITAL = 'hospital', 'Hospital User'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    user_type = models.CharField(
        max_length=10, 
        choices=UserTypeChouse, 
        default=UserTypeChouse.SINGLE
        )  

# Hospital User Model
class HospitalUser(BasicCustomEmployee):
    class Meta:
        verbose_name = _('hospital')
        verbose_name_plural = _('hospitals')

    class ClinicalType(models.TextChoices):
        options1 = 'Options1', 'Options1'
        options2 = 'Options2', 'Options2'
        options3 = 'Options3', 'Options3'
        options4 = 'Options4', 'Options4'
        
    
    class NumStaff(models.TextChoices):
        beginer = '1-5', '1-5'
        medium = '6-10', '6-10'
        large = '11-20', '11-20'
        very_large = '21-50', '21-50'
        huge = '50+', '50+'

    head_physician = models.ForeignKey(
        DrClinicalEmployee, 
        verbose_name=_(""), 
        on_delete=models.CASCADE, 
        related_name='hospital_head_physician'
        )
    clinical_name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50, unique=True)
    clinical_type = models.CharField(choices=ClinicalType)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=10)
    website = models.URLField(blank=True, null=True)
    num_staff = models.CharField(
        _("Num Staff"), 
        max_length=10, 
        choices=NumStaff.choices, 
        default=NumStaff.beginer
        )
    clinical_email = models.EmailField(
        max_length=255,
        blank = False,
        null = True)
    clinical_phone = models.CharField(
        max_length=20,
        blank = False,
        null = True
    )

    def __str__(self):
        return self.clinical_name