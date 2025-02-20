# Generated by Django 5.1.3 on 2025-02-20 08:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduling_date', models.DateField()),
                ('scheduling_time_start', models.TimeField()),
                ('scheduling_time_finish', models.TimeField()),
                ('reserved_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('medication_consultation', models.CharField(choices=[('MICRONUTRIENTS', 'Micronutrients'), ('GENERAL_MEDICINE', 'General Medicine'), ('DERMOCOSMETICS', 'Dermocosmetics'), ('ESTETICS_AND_COSMETICS', 'Estetics and Cosmetics'), ('ANTI_AGING_CONSULTATION', 'Anti-aging Medical Consultation'), ('FOLLOW_UP', 'Follow-up'), ('DERMOCOSMETICS_ONLINE', 'Dermocosmetics Online'), ('ESTETICS_AND_COSMETICS_ONLINE', 'Estetics and Cosmetics Online'), ('FOLLOW_UP_ANTI_AGING', 'Follow-up Anti-aging'), ('FREE_CLINICAL_ASSISTANCE', 'Free Clinical Assistance'), ('MAGRESS_ONLINE', 'Magress Online'), ('HAIR_MEDICINE_AND_TRICHOLOGY', 'Hair Medicine and Trichology'), ('COSMETIC_MICROSURGERY', 'Consultation for Cosmetic Microsurgery')], default='MICRONUTRIENTS')),
                ('price', models.FloatField()),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('CANCELED', 'CANCELED'), ('CONFIRMED', 'CONFIRMED'), ('DONE', 'DONE')], default='PENDING')),
                ('old_procedures', models.CharField(max_length=256)),
                ('comments', models.TextField(blank=True, null=True)),
                ('scheduling_id', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='customer.customers')),
                ('dr_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='employees.drclinicalemployee')),
                ('reserved_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='employees.receptionsclinicalemployee')),
            ],
        ),
    ]
