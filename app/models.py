from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name=models.CharField(max_length=100)

    def __str__(self):
        return self.bank_name
    
class Branch(models.Model):
    bank_name=models.ForeignKey(Bank,on_delete=models.CASCADE,null=False)
    ifsc=models.CharField(max_length=11,primary_key=True)
    branch=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    contact=models.IntegerField()
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    