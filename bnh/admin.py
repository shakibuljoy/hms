from django.contrib import admin

from .models import Doctor, Patient, Bill, BillPayment


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Bill)
admin.site.register(BillPayment)
