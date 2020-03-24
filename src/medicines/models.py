"""
Models related to medicines.
"""

from django.db import models


class Medicine(models.Model):
    name = models.CharField('Medicine Name', max_length=100)
    quantity = models.PositiveIntegerField()
    salt = models.CharField('Salt Information', max_length=200, null=True, blank=True)
    additional_details = models.TextField('Additional Details', null=True, blank=True)

    def __str__(self):
        return self.name
