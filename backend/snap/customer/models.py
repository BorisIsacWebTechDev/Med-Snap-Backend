from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.db import IntegrityError
from autoslug import AutoSlugField
from django.utils.text import slugify
from datetime import datetime

class Customers(models.Model):

    full_name = models.CharField(
        max_length=256
    )

    email = models.EmailField(
        max_length=256,
        blank=True
    )
    tel = models.CharField(null=True, blank=True)
    nif = models.CharField(null=True, blank=True)
    sns = models.CharField(null=True, blank=True)

    address = models.CharField(
        max_length=256
    )

    birthday = models.DateField(null=True, blank=True, default="1900-01-01")

    slug = models.SlugField(max_length=256)

    updated = models.DateTimeField(
        auto_now=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created']
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def save(self, *args, **kwargs):
        # Generate slug if not already set
        if not self.slug:
            self.slug = slugify(f"{self.full_name}-{self.email}")
        try:
            # Attempt to save the instance
            super().save(*args, **kwargs)
        except IntegrityError as e:
            # Handle unique constraint violations gracefully
            if 'unique constraint' in str(e).lower():
                raise ValueError("A customer with this slug already exists.") from e
            raise  # Re-raise other IntegrityErrors

    def create_slug(self):
        base_slug = f"{self.tel}{self.email}{self.nif}"
        return slugify(base_slug)

    def __str__(self):
        return f"{self.full_name}"