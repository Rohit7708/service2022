from sre_constants import CATEGORY
from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=200, null=True)
    password1 = models.CharField(max_length=200, null=True)
    password2 = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    otp=models.CharField(max_length=200,null=True,blank=True)
    uid=models.UUIDField(default=uuid.uuid4)




    def __str__(self):
        return self.username



class Workers(models.Model):
    CATEGORY = (
        ('Cook', 'Cook'),
        ('Full-time Maid', 'Full-time Maid'),
        ('part-time Maid', 'part-time Maid'),
        ('Gardner', 'Gardner'),
    )

    name = models.CharField(max_length=200, null=True)
    age=models.CharField(max_length=200,null=True)
    Domestic=models.CharField(max_length=200,null=True,choices=CATEGORY)
    address=models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return self.name

