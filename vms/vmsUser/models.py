from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

JOUR_PURPOSE = [
    ('Individual', 'Individual'),
    ('Official', 'Official'),
]


class Requisition(models.Model):
    aplctn_date = models.DateTimeField(verbose_name='Requisition Date', null=True, auto_now_add=True)
    jour_purpose = models.CharField(verbose_name='Journey Purpose', max_length=100, choices=JOUR_PURPOSE, blank=True,
                                    null=True)
    jour_date = models.DateField(verbose_name='Journey Date', blank=True, null=True)
    vcl_type = models.CharField(verbose_name='Vehicle Type', max_length=100, blank=True, null=True)
    destination = models.CharField(verbose_name='Destination', max_length=200, blank=True, null=True)
    departr_time = models.TimeField(verbose_name='Departure Time', blank=True, null=True)
    rtrn_time = models.TimeField(verbose_name='Return Time', blank=True, null=True)
    jour_details = models.CharField(verbose_name='Journey Details', max_length=400, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jour_purpose
