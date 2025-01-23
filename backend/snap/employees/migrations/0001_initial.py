# Generated by Django 5.1.3 on 2025-01-14 17:28

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractClinicalEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('contact_number', models.CharField()),
                ('is_staff', models.BooleanField(default=True, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('employee_type', models.CharField(choices=[('Click to select', 'Click to select'), ('DR', 'DR'), ('RECEPTION', 'RECEPTION')], default='Click to select', max_length=50)),
                ('gender_employee', models.CharField(choices=[('Click to select', 'Click to select'), ('Male', 'Male'), ('Female', 'Female')], default='Click to select', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, related_name='clinicalemployee_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='clinicalemployee_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Clinical Employee',
                'verbose_name_plural': 'Clinical Employees',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DRClinicalEmployee',
            fields=[
                ('abstractclinicalemployee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('medical_order_ID', models.CharField(help_text="A unique identifier for the medical order assigned to this user. This ID is used to track the user's medical orders.", unique=True, verbose_name='Medical Order ID')),
                ('speciality_type', models.CharField(choices=[('Click to select', 'Click to select'), ('SPECIALITY1', 'SPECIALITY1'), ('SPECIALITY2', 'SPECIALITY2'), ('SPECIALITY3', 'SPECIALITY3'), ('SPECIALITY4', 'SPECIALITY4'), ('SPECIALITY5', 'SPECIALITY5'), ('SPECIALITY6', 'SPECIALITY6')], default='Click to select', max_length=50)),
            ],
            options={
                'verbose_name': 'DR',
                'verbose_name_plural': "DR's",
            },
            bases=('employees.abstractclinicalemployee',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ReceptionsClinicalEmployee',
            fields=[
                ('abstractclinicalemployee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reception Assistant',
                'verbose_name_plural': "Reception's Assistant",
            },
            bases=('employees.abstractclinicalemployee',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
