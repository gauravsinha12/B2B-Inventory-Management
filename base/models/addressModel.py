from django.db import models
from django.utils import timezone
from localflavor.in_.models import INStateField

class Address(models.Model):
    address = models.TextField(blank=False)
    city = models.CharField(max_length=255, blank=False)
    state = INStateField(blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

    def get_all_address(self):
        return Address.objects.all()
