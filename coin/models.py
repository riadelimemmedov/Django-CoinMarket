from email.policy import default
from django.db import models

# Create your models here.

#!Coin
class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    image = models.URLField(blank=True,null=True)
    price = models.FloatField(default=0,blank=True)
    rank = models.IntegerField(default=0,null=True)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['-rank']
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'