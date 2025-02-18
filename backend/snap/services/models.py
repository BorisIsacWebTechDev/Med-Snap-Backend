import random
import string
from datetime import datetime
from email.policy import default
from random import choices


from django.db.models import CASCADE
from django.utils.timezone import now
from employees.models import SingleUser, ReceptionsClinicalEmployee
from customer.models import Customers

from django.db import models

# Create your models here.
class Services(models.Model):
    CONSULTATION_SPANDING_TIME = {
        'MICRONUTRIENTS': 30,
        'GENERAL_MEDICINE': 40,
        'DERMOCOSMETICS': 45,
        'ESTETICS_AND_COSMETICS': 70,
        'ANTI_AGING_CONSULTATION': 75,
        'FOLLOW_UP': 60,
        'DERMOCOSMETICS_ONLINE': 60,
        'ESTETICS_AND_COSMETICS_ONLINE': 60,
        'FOLLOW_UP_ANTI_AGING': 60,
        'FREE_CLINICAL_ASSISTANCE': 15,
        'MAGRESS_ONLINE': 60,
        'HAIR_MEDICINE_AND_TRICHOLOGY': 60,
        'COSMETIC_MICROSURGERY': 60,
    }

    class MedicalConsultations(models.TextChoices):
        MICRONUTRIENTS = 'MICRONUTRIENTS', 'Micronutrients'
        GENERAL_MEDICINE = 'GENERAL_MEDICINE', 'General Medicine'
        DERMOCOSMETICS = 'DERMOCOSMETICS', 'Dermocosmetics'
        ESTETICS_AND_COSMETICS = 'ESTETICS_AND_COSMETICS', 'Estetics and Cosmetics'
        ANTI_AGING_CONSULTATION = 'ANTI_AGING_CONSULTATION', 'Anti-aging Medical Consultation'
        FOLLOW_UP = 'FOLLOW_UP', 'Follow-up'
        DERMOCOSMETICS_ONLINE = 'DERMOCOSMETICS_ONLINE', 'Dermocosmetics Online'
        ESTETICS_AND_COSMETICS_ONLINE = 'ESTETICS_AND_COSMETICS_ONLINE', 'Estetics and Cosmetics Online'
        FOLLOW_UP_ANTI_AGING = 'FOLLOW_UP_ANTI_AGING', 'Follow-up Anti-aging'
        FREE_CLINICAL_ASSISTANCE = 'FREE_CLINICAL_ASSISTANCE', 'Free Clinical Assistance'
        MAGRESS_ONLINE = 'MAGRESS_ONLINE', 'Magress Online'
        HAIR_MEDICINE_AND_TRICHOLOGY = 'HAIR_MEDICINE_AND_TRICHOLOGY', 'Hair Medicine and Trichology'
        COSMETIC_MICROSURGERY = 'COSMETIC_MICROSURGERY', 'Consultation for Cosmetic Microsurgery'

    class StatusOptions(models.TextChoices):
        pending = "PENDING", "PENDING"
        canceled = "CANCELED", "CANCELED"
        confirmed = "CONFIRMED", "CONFIRMED"
        done = "DONE", "DONE"

    scheduling_date = models.DateField()

    scheduling_time_start = models.TimeField()
    scheduling_time_finish = models.TimeField()

    reserved_on = models.DateTimeField(default=now)

    reserved_by = models.ForeignKey(
        ReceptionsClinicalEmployee,
        related_name="+",
        on_delete=models.RESTRICT,
    )

    medication_consultation = models.CharField(
        choices=MedicalConsultations,
        default=MedicalConsultations.MICRONUTRIENTS
    )

    price = models.FloatField()

    dr_id = models.ForeignKey(
        SingleUser,
        related_name="+",
        on_delete= models.RESTRICT,
    )

    customer_id = models.ForeignKey(
        Customers,
        related_name="+",
        on_delete=models.RESTRICT,
    )

    status = models.CharField(
        choices=StatusOptions,
        default=StatusOptions.pending
    )

    old_procedures = models.CharField(max_length=256)


    comments = models.TextField(
        blank=True,
        null=True
    )


    scheduling_id = models.CharField(
        max_length=10
    )

    def scheduling_id_generator(self):
        res = ''
        rand_digits = string.ascii_letters + string.digits
        for obj in range(7):
            new_digit = random.choices(rand_digits)[0]
            res += new_digit
            print('Scheduling ID has been generated', res)
        return res

    def getter_scheduling_id_generator(self):
        return self.scheduling_id_generator()


    def save(self,*args,**kwargs):
        if not self.scheduling_id:
            self.scheduling_id = self.generate_scheduling_id()
        super().save(*args, **kwargs)

