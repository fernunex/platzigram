"""Posts models."""

#Django
from django.db import models
# Create your models here.




class User(models.Model):
    """User model."""

    MEXICO = 'MX'
    UNITED_STATES_OF_AMERICA = 'US'
    COLOMBIA = 'CL'
    VENEZUELA = 'VZ'
    ARGENTINA = 'AR'
    BRAZIL = 'BR'
    COUNTRY_CHOICES=(
                    (MEXICO,'Mexico'),
                    (UNITED_STATES_OF_AMERICA,'United States'),
                    (COLOMBIA,'Colombia'),
                    (VENEZUELA,'Venezuela'),
                    (ARGENTINA,'Argentina'),
                    (BRAZIL,'Brazil')
                    )

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(
        max_length = 2,
        choices = COUNTRY_CHOICES,
        default = MEXICO
    )

    is_admin = models.BooleanField(default=True)

    bio = models.TextField()

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

