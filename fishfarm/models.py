from django.db import models


class ManageStaff(models.Model):
    staffid=models.CharField(max_length=50)
    staffname=models.TextField()
    staffEmail=models.EmailField()
    staffImage=models.ImageField(upload_to="image/")
    def __str__(self):
        return self.staffname

class ManageDam(models.Model):
    damName=models.TextField()
    damLocation=models.TextField()
    damHeight=models.FloatField()
    def __str__(self):
        return self.damName

class ManageDepartment(models.Model):
    departmentName=models.TextField()
    departmentCount=models.IntegerField()
    def __str__(self):
        return self.departmentName

class ManageFish(models.Model):
    fishName=models.TextField()
    fishCount=models.IntegerField()
    fishSold=models.IntegerField()
    def __str__(self):
        return self.fishName

class ManageSales(models.Model):
    fishName = models.TextField()
    fishSales=models.FloatField()
    salesDate=models.DateField()
    def __str__(self):
        return self.fishName

class ManageCredit(models.Model):
    creditYear=models.TextField()
    totalCredit=models.FloatField()
    def __str__(self):
        return self.creditYear

class ManageTimeline(models.Model):
    harvestTime=models.DateField()
    fishType=models.TextField()
    def __str__(self):
        return self.harvestTime
