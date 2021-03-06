"""Models related to medicines app."""

from django.db import models


class Medicine(models.Model):
    name = models.CharField('Medicine Name', max_length=100)
    quantity = models.PositiveIntegerField()
    salt = models.CharField(
        'Salt Information',
        max_length=200,
        null=True,
        blank=True,
    )
    additional_details = models.TextField(
        'Additional Details',
        null=True,
        blank=True,
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        name = self.name
        if self.salt:
            name = f'{name} - {self.salt}'
        return name
