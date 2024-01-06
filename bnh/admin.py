from django.contrib import admin

from .models import Doctor, Patient, Bill, BillPayment, ItemCount, Item


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Bill)
admin.site.register(BillPayment)
admin.site.register(ItemCount)
admin.site.register(Item)
