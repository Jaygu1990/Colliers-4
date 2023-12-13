from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username







# Create your models here.
def upload_to_w9(instance, filename):
    return f'media/PDF/W9/{filename}'

def upload_to_tin_check(instance, filename):

    return f'media/PDF/TIN/{filename}'

def upload_to_license_check(instance, filename):

    return f'media/PDF/License/{filename}'

def upload_to_others(instance, filename):

    return f'media/PDF/Others/{filename}'

def upload_to_ACH(instance, filename):

    return f'media/PDF/ACH/{filename}'

class vendorRequest(models.Model):
    deal_number = models.PositiveIntegerField()
    vendor_name = models.CharField(max_length=256)
    vendor_code = models.CharField(max_length=256, blank=True)
    vendor_address = models.CharField(max_length=256, blank=True)
    date = models.DateField(default="1990-01-01")

    W9 = models.FileField(upload_to=upload_to_w9, blank=True)
    TIN_check = models.FileField(upload_to=upload_to_tin_check, blank=True)
    license_check = models.FileField(upload_to=upload_to_license_check, blank=True)
    ACH = models.FileField(upload_to=upload_to_ACH, blank=True)
    others = models.FileField(upload_to=upload_to_others, blank=True)

    expiration_date = models.DateField(default="1990-01-01",blank=True,null=True)
    State = models.CharField(max_length=256, blank=True)
    Country = models.CharField(max_length=256, blank=True)
    Note = models.CharField(max_length=256, blank=True)


    request_person = models.CharField(max_length=256)
    prepare_person = models.CharField(max_length=256, blank=True)
    approve_person = models.CharField(max_length=256, blank=True)

    status = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.vendor_name


class AXvendor(models.Model):
    vendor_name = models.CharField(max_length=256)
    vendor_code = models.CharField(max_length=256)
    vendor_address = models.CharField(max_length=256)
    vendor_type = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.vendor_name

