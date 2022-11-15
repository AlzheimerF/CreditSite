from django.db import models
from user.models import Profile

class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    CURRENCY_CHOICES = [
        ('EUR', 'EUR'),
        ('RUB', 'RUB'),
        ('US', 'US'),
        ('KZ', 'KZ'),
    ]
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(unique=True)
    summ = models.DecimalField(unique=True, decimal_places=2, max_digits=2)
    percent = models.DecimalField(unique=True, decimal_places=2, max_digits=2)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=50, unique=True)
    datetime = models.DateTimeField(auto_now_add=True, unique=True)
    term_of_conditions = models.IntegerField(unique=True)
    status = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.title

class Order(models.Model):
    user_giving = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='giving')
    user_taking = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='taking')
    STATUS_CHOICES = [
        ('IN ACTION', 'IN ACTION'),
        ('FINISHED', 'FINISHED'),
        ('CANCELED', 'CANCELED'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)

