from .models import Sbiaccount,IoBaccount,Transaction

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
    
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['trans_type', 'description', 'receiver_name', 'receiver_amount']
        widgets = {
            'trans_type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'padding: 12px; border-radius: 8px; border: 2px solid #e0e0e0;'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter transaction description',
                    'style': 'padding: 12px; border-radius: 8px; border: 2px solid #e0e0e0;'
                }
            ),
            'receiver_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter receiver name',
                    'style': 'padding: 12px; border-radius: 8px; border: 2px solid #e0e0e0;'
                }
            ),
            'receiver_amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter amount',
                    'min': '0',
                    'step': '0.01',
                    'style': 'padding: 12px; border-radius: 8px; border: 2px solid #e0e0e0;'
                }
            ),
        }
        labels = {
            'trans_type': 'Transaction Type',
            'description': 'Description',
            'receiver_name': 'Receiver Name',
            'receiver_amount': 'Amount (₹)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trans_type'].choices = Transaction.TYPE_CHOICES
        for field in self.fields.values():
            field.required = True
        self.fields['description'].required = False