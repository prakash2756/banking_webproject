import random
from django.db import models

# Create your models here.

def generateAccountNumber():
    from .models import Sbiaccount,IoBaccount
    
    while True:
        account_num = str(random.randint(10**11,(10**12)-1))
        if not Sbiaccount.objects.filter(account_number=account_num).exists() and not IoBaccount.objects.filter(account_number=account_num).exists():
            return account_num    
    

class Sbiaccount(models.Model):
        account_name = models.CharField(max_length=200)
        dob = models.DateField(null=True, blank=True)
        phone_number = models.CharField(max_length=12,blank=True,null=True)
        email_address =models.EmailField(max_length=200,unique=True)
        address = models.CharField(max_length=200,blank=True,null=True)
        city = models.CharField(max_length=200,blank=True,null=True)
        pan = models.CharField(max_length=20,blank=True,null=True)
        aadhaar = models.CharField(max_length=12,blank=True,null=True)
        account_request = models.DateTimeField(auto_now_add=True)
        bank_name = models.CharField(max_length=200,default='SBI')
        account_number = models.CharField(max_length=12, unique=True, blank=True)
        
        def save(self,*args, **kwargs):
            if not self.account_number:
                self.account_number=generateAccountNumber()                
            super().save(*args, **kwargs)
        
        def __str__(self):
            return f"{self.account_name}{self.bank_name}{self.dob}{self.account_request}{self.email_address}"
        
        
        
class IoBaccount(models.Model):
        account_name = models.CharField(max_length=200)
        dob = models.DateField(null=True, blank=True)
        phone_number = models.CharField(max_length=12,blank=True,null=True)
        email_address =models.EmailField(max_length=200,unique=True)
        address = models.CharField(max_length=200,blank=True,null=True)
        city = models.CharField(max_length=200,blank=True,null=True)
        pan = models.CharField(max_length=20,blank=True,null=True)
        aadhaar = models.CharField(max_length=12,blank=True,null=True)
        account_request = models.DateTimeField(auto_now_add=True)
        bank_name = models.CharField(max_length=200,default='IOB')
        account_number = models.CharField(max_length=12, unique=True, blank=True)
        
        
        def save(self,*args, **kwargs):
            if not self.account_number:
                self.account_number=generateAccountNumber()                
            super().save(*args, **kwargs)
        
        def __str__(self):
            return f"{self.account_name}{self.bank_name}{self.dob}{self.account_request}{self.email_address}"

