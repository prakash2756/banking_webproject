from .models import Sbiaccount,IoBaccount

from django import forms



class SbiAccountForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%d-%m-%Y'],widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'DD-MM-YYYY'}))
    class Meta:
        model = Sbiaccount
        fields = ['account_name','dob','email_address','bank_name']
        widgets = {            
                    'account_name':forms.TextInput(attrs={
                        'placeholder':'Enter you name as per Adhear',
                        'required':'required'
                    }),
                    
                    'email_address':forms.EmailInput(attrs={
                        'placeholder':'Please update your Email address',
                        'required':'required'
                    }),
                            
                }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.bank_name = "SBI"  # auto-assign
        if commit:
            instance.save()
        return instance
            
        
        
class IobAccountForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%d-%m-%Y'],widget=forms.DateInput(format='%d-%m-%Y', attrs={'placeholder': 'DD-MM-YYYY'}))
    class Meta:
        model = IoBaccount
        fields = ['account_name','dob','email_address','bank_name']
        widgets = {            
                    'account_name':forms.TextInput(attrs={
                        'placeholder':'Enter you name as per Adhear',
                        'required':'required'
                    }),
                    
                    'email_address':forms.EmailInput(attrs={
                        'placeholder':'Please update your Email address',
                        'required':'required'
                    }),
                            
                }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.bank_name = "IOB   "  # auto-assign
        if commit:
            instance.save()
        return instance
    
    
    
