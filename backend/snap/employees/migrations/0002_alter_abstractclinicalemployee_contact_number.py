# Generated by Django 5.1.3 on 2025-01-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractclinicalemployee',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
