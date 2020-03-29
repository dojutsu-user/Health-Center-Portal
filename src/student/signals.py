"""Signals related to student app."""

from django.db.models.signals import post_save

from medicines.models import Medicine
from student.models import VisitHistory


def update_medicines_quantity(sender, instance, created, *args, **kwargs):
    """Updates the quantity of medicine after it has been given to the student."""

    if created:
        medicines_qs = instance.medicinegivenhistory_set.all()
        if medicines_qs.exists():
            for data in medicines_qs:
                medicine_obj = data.medicine
                medicine_obj.quantity -= data.quantity
                medicine_obj.save()


post_save.connect(update_medicines_quantity, sender=VisitHistory)
