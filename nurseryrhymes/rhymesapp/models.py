from django.db import models
from django.contrib.auth.models import User



class Rhyme(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    premium = models.BooleanField(default=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)