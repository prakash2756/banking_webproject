from django.contrib import admin
from .models import Sbiaccount,IoBaccount,Transaction

# Register your models here.
admin.site.register(Sbiaccount)
admin.site.register(IoBaccount)
admin.site.register(Transaction)


