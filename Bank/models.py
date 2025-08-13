from django.db import models

# Create your models here.

class Sbiaccount(models.Model):
        account_name = models.CharField(max_length=200)
        dob = models.DateField(null=True, blank=True)
        email_address =models.EmailField(max_length=200,unique=True)
        account_request = models.DateTimeField(auto_now_add=True)
        bank_name = models.CharField(max_length=200,default='SBI')
        
        
        def __str__(self):
            return f"{self.account_name}{self.bank_name}{self.dob}{self.account_request}{self.email_address}"
        
        
        
class IoBaccount(models.Model):
        account_name = models.CharField(max_length=200)
        dob = models.DateField(null=True, blank=True)
        email_address =models.EmailField(max_length=200,unique=True)
        account_request = models.DateTimeField(auto_now_add=True)
        bank_name = models.CharField(max_length=200,default='IOB')
        
        def __str__(self):
            return f"{self.account_name}{self.bank_name}{self.dob}{self.account_request}{self.email_address}"

