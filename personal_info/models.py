from django.db import models


# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    occupation = models.CharField(max_length=100, null=False, blank=False)
    name_of_employer = models.CharField(max_length=100, null=False, blank=False)
    job_title = models.CharField(max_length=100, null=False, blank=False)
    sin_number = models.CharField(max_length=100, null=False, blank=False)
    income = models.DecimalField(max_digits=10, max_length=20,decimal_places=3)

