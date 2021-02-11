from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    num_doc = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=20)
