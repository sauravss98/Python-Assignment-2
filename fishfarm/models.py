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
    fishSales=models.FloatField()
    def __str__(self):
        return self.fishSales

class ManageCredit(models.Model):
    totalCredit=models.FloatField()
    def __str__(self):
        return self.totalCredit

class ManageTimeline(models.Model):
    harvestTime=models.DateField()
    def __str__(self):
        return self.harvestTime
