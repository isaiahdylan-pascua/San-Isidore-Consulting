from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxLengthValidator

# Create your models here.

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True) 
    ProductName = models.CharField(max_length=30, null=False, blank=False)
    ProductCost = models.FloatField(max_length=6,null=False, blank=False)
    ProductStock = models.IntegerField(null=False, blank=False)
    objects = models.Manager()
    
    def getID(self):
        return self.pk

    def getName(self):
        return self.ProductName
    
    def getCost(self):
        return self.ProductCost

    def getStock(self):
        return self.ProductStock

    def __str__(self):
        return "ProductID: "+str(self.pk) + " Name: " + str(self.ProductName) + " |Php: " +str(self.ProductCost) + " |Stock Remaining: " + str(self.ProductStock)


class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Date = models.DateTimeField(auto_now=True)
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

class Stocks(models.Model):
    StockID = models.AutoField(primary_key=True)
    Stockname = models.CharField(max_length=30, null=False, blank=False)
    Stockqty = models.IntegerField(null=False, blank=False)
    objects = models.Manager()

    def getSID(self):
        return self.StockID

    def getStockname(self):
        return self.Stockname
    
    def getSQty(self):
        return self.Stockqty

    def __str__(self):
        return "ID: " + str(self.StockID) + " Stock: " + str(self.Stockname) + " Amount: " + str(self.Stockqty)

class EmployeeUserManager(BaseUserManager):
    def create_user(self, EmployeeID, password, EmployeeName,
                    Occupation, DateofEmployment, EmployeeStreet, EmployeeBarangay,
                    EmployeeCity, EmployeeProvince, EmployeeZipCode):
        user = self.model(EmployeeID=EmployeeID,
                          EmployeeName=EmployeeName,
                          Occupation=Occupation,
                          DateofEmployment=DateofEmployment,
                          EmployeeStreet=EmployeeStreet,
                          EmployeeCity=EmployeeCity,
                          EmployeeProvince=EmployeeProvince,
                          EmployeeZipCode=EmployeeZipCode
                          )
        if not EmployeeID:
            raise ValueError('Users must have an ID')
        elif not EmployeeName:
            raise ValueError('Users must have a name')
        elif not Occupation:
            raise ValueError('Users must provide their occupation')
        elif not DateofEmployment:
            raise ValueError('Users must provide their date of employment')
        elif not EmployeeStreet:
            raise ValueError('Users must provide their full address (including their street)')
        elif not EmployeeCity:
            raise ValueError('Users must provide their full address (including their city)')
        elif not EmployeeProvince:
            raise ValueError('Users must provide their full address (including their province)')
        elif not EmployeeZipCode:
            raise ValueError('Users must provide their full address (including their zip code)')

        user.set_password(password)
        user.save(using=self.db)
        return user 
    

    def create_superuser(self, EmployeeID, password, EmployeeName,
                    Occupation, DateofEmployment, EmployeeStreet, EmployeeBarangay,
                    EmployeeCity, EmployeeProvince, EmployeeZipCode):
        user = self.model(EmployeeID=EmployeeID,
                          EmployeeName=EmployeeName,
                          Occupation=Occupation,
                          DateofEmployment=DateofEmployment,
                          EmployeeStreet=EmployeeStreet,
                          EmployeeCity=EmployeeCity,
                          EmployeeProvince=EmployeeProvince,
                          EmployeeZipCode=EmployeeZipCode
                          )
        user.is_admin = True
        user.save(using=self.db)
        return user
        

class Employee(AbstractBaseUser):
    EmployeeID = models.IntegerField(verbose_name = "Employee ID", primary_key=True, unique=True, validators=[MaxLengthValidator(6)])
    EmployeeName = models.CharField(max_length = 30, verbose_name = "Employee Name")
    Occupation = models.CharField(max_length = 30, verbose_name = "Occupation")
    DateofEmployment = models.DateField(verbose_name = "Date of Employment")
    EmployeeStreet = models.CharField(max_length = 30, verbose_name = "Street Address")
    EmployeeBarangay = models.CharField(max_length = 30, verbose_name = "Barangay Address")
    EmployeeCity = models.CharField(max_length = 30, verbose_name = "City/Municipality Address")
    EmployeeProvince = models.CharField(max_length = 30, verbose_name = "Province Address")
    EmployeeZipCode = models.IntegerField(verbose_name = "Zip Code", validators=[MaxLengthValidator(6)])
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "EmployeeID"
    REQUIRED_FIELDS = ["EmployeeName", "Occupation","DateofEmployment","EmployeeStreet",
                       "EmployeeBarangay","EmployeeCity","EmployeeProvince","EmployeeZipCode"]

    def __str__(self):
        return "ID:" + str(self.EmployeeID + ";" + str("EmployeeName"))
