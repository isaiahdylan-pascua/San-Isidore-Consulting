from django.db import models

# Create your models here.

class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True, max_length= 6, default=1000) 
    ProductName = models.CharField(max_length=30)
    ProductCost = models.FloatField(max_length=6)
    objects = models.Manager()

    def getID(self):
        return self.ProductID

    def getName(self):
        return self.ProductName
    
    def getCost(self):
        return self.ProductCost





