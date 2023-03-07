from django.db import models

# Create your models here.

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True) 
    ProductName = models.CharField(max_length=30, null=False, blank=False)
    ProductCost = models.FloatField(max_length=6,null=False, blank=False)
    objects = models.Manager()
    
    

    
    def getID(self):
        return self.pk

    def getName(self):
        return self.ProductName
    
    def getCost(self):
        return self.ProductCost

    def __str__(self):
        return str(self.pk) + self.ProductName + str(self.ProductCost)





