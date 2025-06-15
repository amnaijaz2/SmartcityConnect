from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class ServiceProviderR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service_image = models.ImageField(upload_to='service_images/')
    servicename = models.CharField(max_length=100)  # This can be the name of the service
    Phoneno = models.CharField(max_length=15)
    address = models.TextField()
   

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  # Hash the password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)  # Verify the password
