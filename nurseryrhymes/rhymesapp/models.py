from django.db import models
from django.utils import timezone


# Account model.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    zipcode = models.CharField(max_length=5)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name)


class Rhyme(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=100)

