from django.db import models
from autoutilitare.models import Autoutilitare




class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField()
    driver_license = models.IntegerField()
    drivers_validity_license = models.DateTimeField()
    country_of_residence = models.CharField(max_length=30)  # aici de pus dropdown cu tarile
    # start_date = models.DateField()
    # end_date = models.DateField()
    car = models.ForeignKey(Autoutilitare, on_delete=models.CASCADE)


    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




