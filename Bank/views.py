from django.shortcuts import render,redirect
from django.core.cache import cache
from django.http import HttpResponse
from .forms import IobAccountForm,SbiAccountForm,TransactionForm
from.models import Sbiaccount,IoBaccount,Transaction
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum, Q
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def createaccount(request):
    if request.method =="POST":
        bank_type = request.POST.get('bank_type')
        if bank_type=='SBI':
            print('yes bi')
            form = SbiAccountForm(request.POST)
            if form.is_valid():
                print('yes')
                account = form.save()                
                request.session['account_id'] = account.id
                request.session['bank_type'] = 'SBI'
                return redirect('success')
            else:
                return render(request, 'create-account.html', {
                    'sbi_form': form,
                    'iob_form': IobAccountForm()
                })          
        elif bank_type=='IOB':
            form = IobAccountForm(request.POST)
            if form.is_valid():
                account=form.save()
                request.session['account_id'] = account.id
                request.session['bank_type'] = 'IOB'
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
    account_type = request.session.get('bank_type')
    account_id = request.session.get('account_id')
    if not account_type or not  account_id :
        return redirect('create-account')
    if account_type=='SBI':
        print('yes sbi')
        account =Sbiaccount.objects.get(id=account_id)
    if account_type=='IOB':
        print('Yes IOB')
        account = IoBaccount.objects.get(id=account_id)
        
    
        
    return render(request,'success.html',{'context':account})


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
    
    if account_type == 'SBI':
        account = Sbiaccount.objects.get(id=account_id)
        content_type = ContentType.objects.get_for_model(Sbiaccount)
    if account_type=="IOB":
        account = IoBaccount.objects.get(id=account_id)
        content_type = ContentType.objects.get_for_model(IoBaccount)
    
    # Get all transactions for this account
    transactions = Transaction.objects.filter(
        content_type=content_type,
        object_id=account_id
    ).order_by('-tran_date')[:10]  # Get last 10 transactions
    
    # Calculate account balance
    credits = Transaction.objects.filter(
        content_type=content_type,
        object_id=account_id,
        trans_type=Transaction.CREDIT
    ).aggregate(total=Sum('receiver_amount'))['total'] or 0
    
    debits = Transaction.objects.filter(
        content_type=content_type,
        object_id=account_id,
        trans_type=Transaction.DEBIT
    ).aggregate(total=Sum('receiver_amount'))['total'] or 0
    
    # Convert to float for calculation (assuming receiver_amount is stored as string)
    try:
        credits = float(credits) if credits else 0
        debits = float(debits) if debits else 0
    except (ValueError, TypeError):
        credits = 0
        debits = 0
    
    balance = credits - debits
    
    # Get transaction counts
    total_transactions = transactions.count()
    credit_count = Transaction.objects.filter(
        content_type=content_type,
        object_id=account_id,
        trans_type=Transaction.CREDIT
    ).count()
    
    debit_count = Transaction.objects.filter(
        content_type=content_type,
        object_id=account_id,
        trans_type=Transaction.DEBIT
    ).count()
    
    context = {
        'account': account,
        'transactions': transactions,
        'balance': balance,
        'total_transactions': total_transactions,
        'credit_count': credit_count,
        'debit_count': debit_count,
        'credits_total': credits,
        'debits_total': debits,
    }
    
    return render(request, 'welcome-page.html', {'context': context})


def add_transaction(request):
    account_type = request.session.get('account_type')
    account_id = request.session.get('account_id')
    
    if not account_type or not account_id:
        messages.error(request, 'Please login to access your account.')
        return redirect('login-form')
    
    if account_type == 'SBI':
        account = Sbiaccount.objects.get(id=account_id)
        content_type = ContentType.objects.get_for_model(Sbiaccount)
    else:
        account = IoBaccount.objects.get(id=account_id)
        content_type = ContentType.objects.get_for_model(IoBaccount)
    
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.content_type = content_type
            transaction.object_id = account_id
            transaction.save()
            
            if transaction.trans_type =='CR':            
                messages.success(request, f'Transaction of ₹{transaction.receiver_amount} Credited successfully!')
            else:
                messages.error(request, f'Transaction of ₹{transaction.receiver_amount} Debited successfully!')
            return redirect('welcome-page')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = TransactionForm()
    
    context = {
        'form': form,
        'account': account,
    }
    
    return render(request, 'add-transaction.html', context)



def logout_view(request):
    request.session.flush() 
    cache.clear()
    messages.success(request, 'You have been logged out.')    
    return redirect('login-form')