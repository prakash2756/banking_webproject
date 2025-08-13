from .models import Sbiaccount,IoBaccount

from django import forms



class SbiAccountForm(forms.ModelForm):
    dob = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y', attrs={
            'placeholder': 'DD-MM-YYYY',
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = Sbiaccount
        fields = ['account_name', 'dob', 'email_address', 'phone_number', 'address', 'city', 'pan', 'aadhaar']
        widgets = {
            'account_name': forms.TextInput(attrs={
                'placeholder': 'Enter your name as per Aadhaar',
                'class': 'form-control'
            }),
            'email_address': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter your address',
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city',
                'class': 'form-control'
            }),
            'pan': forms.TextInput(attrs={
                'placeholder': 'Enter PAN number',
                'class': 'form-control'
            }),
            'aadhaar': forms.TextInput(attrs={
                'placeholder': 'Enter Aadhaar number',
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.bank_type = "SBI"
        if commit:
            instance.save()
        return instance

class IobAccountForm(forms.ModelForm):
    dob = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format='%d-%m-%Y', attrs={
            'placeholder': 'DD-MM-YYYY',
            'class': 'form-control'
        })
    )
    
    class Meta:
        model = IoBaccount
        fields = ['account_name', 'dob', 'email_address', 'phone_number', 'address', 'city', 'pan', 'aadhaar']
        widgets = {
            'account_name': forms.TextInput(attrs={
                'placeholder': 'Enter your name as per Aadhaar',
                'class': 'form-control'
            }),
            'email_address': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address',
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter phone number',
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter your address',
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'placeholder': 'Enter your city',
                'class': 'form-control'
            }),
            'pan': forms.TextInput(attrs={
                'placeholder': 'Enter PAN number',
                'class': 'form-control'
            }),
            'aadhaar': forms.TextInput(attrs={
                'placeholder': 'Enter Aadhaar number',
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.bank_type = "IOB"
        if commit:
            instance.save()
        return instance