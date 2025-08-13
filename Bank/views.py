from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import IobAccountForm,SbiAccountForm
from.models import Sbiaccount,IoBaccount
from django.contrib import messages

# Create your views here.


def createaccount(request):
    if request.method =="POST":
        bank_type = request.POST.get('bank_type')
        if bank_type=='SBI':
            print('yes bi')
            form = SbiAccountForm(request.POST)
            if form.is_valid():
                print('yes')
                form.save()
                return redirect('success')  
            else:
                return render(request, 'create-account.html', {
                    'sbi_form': form,
                    'iob_form': IobAccountForm()
                })          
        elif bank_type=='IOB':
            form = IobAccountForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')
            else:
                return render(request, 'create-account.html', {
                    'sbi_form': form,
                    'iob_form': IobAccountForm()
                })
            
    sbi_form = SbiAccountForm()
    iob_form = IobAccountForm()
    return render(request,'create-account.html',{'sbi_form':sbi_form,'iob_form':iob_form})


def success(request):
    return render(request,'success.html')


def loginpage(request):
    if request.method =="POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        account_type = request.POST.get('bank_type')
        if account_type =='SBI':
            sbi_acc = Sbiaccount.objects.filter(account_name=username,email_address=email).first()
            if sbi_acc:
                request.session['account_type']='SBI'
                request.session['account_id']=sbi_acc.id
                return redirect('welcome-page')
            
        if account_type =='IOB':
            iob_acc = IoBaccount.objects.filter(account_name=username,email_address=email).first()
            if iob_acc:
                request.session['account_type']='IOB'
                request.session['account_id']=iob_acc.id
                return redirect('welcome-page')
            
        
        messages.error(request,"Please check the Username, Email and Bank Name")
        
        
    return render(request,'login-form.html')


def welcomepage(request):
    account_type = request.session.get('account_type')
    account_id = request.session.get('account_id')
    if account_type=='SBI':
        account =Sbiaccount.objects.get(id=account_id)        
    else:
        account = IoBaccount.objects.get(id=account_id)
    
    return render(request,'welcome-page.html',{'context':account})
            
