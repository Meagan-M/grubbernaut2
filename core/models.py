from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    """       """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    

    def __str__(self):
        """    """
        return self.user.username

    

