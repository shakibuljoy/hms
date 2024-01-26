from django.urls import path
from .views import (home, doctor_create, patient_create, bill_create, bill_list, bill_payment,
                     bill_pdf, item_list, item_create, get_price, patient_list,
                     patient_detail, summary
                     )


app_name = 'bnh'

urlpatterns = [
    path('', summary, name='home'),
    path('patient/', patient_list, name='patient-list'),
    path('patient/detail/<pk>/', patient_detail, name='patient-detail'),
    path('doctor/', doctor_create, name='doctor'),
    path('patient-create/', patient_create, name='create-patient'),
    path('bill-create/<pk>/', bill_create, name='create-bill'),
    path('bill-list/<pk>/', bill_list, name='bill-list'),
    path('bill-payement/<pk>/', bill_payment, name='bill-payment'),
    path('bill-pdf/<pk>/', bill_pdf, name='bill-pdf'),
    path('item-create/', item_create, name='item-create'),
    path('item-list/', item_list, name='item-list'),
    path('get_price/<pk>/', get_price, name='get-price'),
]
