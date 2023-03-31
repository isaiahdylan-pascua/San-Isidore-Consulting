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
        return "ProductID: "+str(self.pk) + " Name: " + str(self.ProductName) + " |Php: " +str(self.ProductCost)

class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Date = models.DateField(auto_now=True)
    Server = models.CharField(max_length=30, blank=False)
    Table = models.CharField(max_length=30, blank=False)
    PaymentOption = models.CharField(max_length=30, blank=False)
    PWDS = models.CharField(max_length=30, blank=False)
    Tendered = models.FloatField(null=True)
    objects = models.Manager()

    def getID(self):
        return self.pk

    def getDate(self):
        return self.Date
    
    def getServer(self):
        return self.Server

    def getTable(self):
        return self.Table

    def getOption(self):
        return self.PaymentOption

    def getPWDS(self):
        return self.PWDS

    def getTendered(self):
        return self.Tendered

    def __str__(self):
        return "OrderID: "+str(self.pk) + " |Y-M-D: " + str(self.Date) + " |Server: " +str(self.Server) + " |Table No.: " + str(self.Table) + " |Paid: " + str(self.Tendered) + " via " + str(self.PaymentOption) + str(self.PWDS)


# class Orderlines(models.Model):
#     OrderID = models.ForeignKey('Orders',on_delete=models.CASCADE)
#     ProductID = models.ForeignKey('Product',on_delete=models.CASCADE)
#     ProductQty = models.IntegerField(null=False, blank=False)
#     Discount = models.BooleanField()
#     objects = models.Manager()


class Orderlines(models.Model):
    OrderID = models.IntegerField(null=False, blank=False)
    Product = models.IntegerField(null=False, blank=False)
    ProductCost = models.FloatField()
    ProductDesc = models.CharField(max_length=30, blank=True)
    ProductQty = models.IntegerField(null=False, blank=False)
    Discount = models.CharField(max_length=30, blank=True)
    Finalprice = models.FloatField()
    objects = models.Manager()
    
    def getOID(self):
        return self.OrderID

    def getP(self):
        return self.Product
    
    def getPQty(self):
        return self.ProductQty
    
    def getDsc(self):
        return self.Discount

    def __str__(self):
        return "OrderID: " + str(self.OrderID) + " |ProductID: " + str(self.Product) + " |Quantity: " + str(self.ProductQty) + " |Discounted: " + str(self.Discount)