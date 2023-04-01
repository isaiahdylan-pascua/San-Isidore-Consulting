from django.db import models

# Create your models here.

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True) 
    ProductName = models.CharField(max_length=30, null=False, blank=False)
    ProductCost = models.FloatField(max_length=6,null=False, blank=False)
    objects = models.Manager()
    
    

    
    def getID(self):
        return self.ProductID

    def getName(self):
        return self.ProductName
    
    def getCost(self):
        return self.ProductCost

    def __str__(self):
        return f"{self.ProductID}, {self.ProductName}, {self.ProductCost}"





<<<<<<< Updated upstream
=======
    def getP(self):
        return self.Product
    
    def getPQty(self):
        return self.ProductQty
    
    def getDsc(self):
        return self.Discount

    def __str__(self):
        return "OrderID: " + str(self.OrderID) + " |ProductID: " + str(self.Product) + " |Quantity: " + str(self.ProductQty) + " |Discounted: " + str(self.Discount)
    
class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True, unique=True)
    password = models.CharField(max_length=8)
    objects = models.Manager()
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password 
    def __str__(self):
        return 'pk: ' + str(self.pk) + ': ' + self.username 
    
>>>>>>> Stashed changes
