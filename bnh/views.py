from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm, PatientForm, BillForm, BillPaymentForm, ItemForm, item_formset
from .models import Doctor, Patient, Bill, Item, ItemCount, BillPayment
from django.contrib import messages
from django.db.models import Q
from datetime import datetime


def home(request):
    patient = Patient.objects.all()
    context = {
        'patient_list': patient
    }
    return render(request, 'home.html', context)


def patient_list(request):
    filter_type = request.GET.get('type')
    if filter_type:
        patient_list = Patient.objects.filter(patient_type=filter_type)
    else:
        patient_list = Patient.objects.all()
    context = {
        'patient_list':patient_list
    }
    return render(request, 'patient_list.html', context)

def patient_detail(request,pk):
    patient = get_object_or_404(Patient, pk=pk)
    meta_fields = patient._meta.fields
    context = {
        'patient':patient,
        'meta_fields': meta_fields
    }
    return render(request, 'patient_detail.html', context)

@login_required
def doctor_create(request):
    doctor_list = Doctor.objects.all()
    form = DoctorForm()
    if request.POST:
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Doctor Created")
    context = {
        'doctors': doctor_list,
        'form': form
    }
    return render(request, 'doctor.html', context)

@login_required
def patient_create(request):
    form = PatientForm()
    if request.POST:
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bnh:patient-list')
    return render(request, 'partials/create_patient.html', {'form':form})


@login_required
def item_create(request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Succesfully saved!")
            return redirect('bnh:item-list')
    context = {
        'form': ItemForm()
    }
    return render(request, 'partials/item_create.html', context)

@login_required
def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'item_list.html', context)

@login_required
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    total_amount = 0
    total_unit = 0
    try:
        item_count = ItemCount.objects.filter(item=item)
        for i in item_count:
            total_amount += i.amount()
            total_unit += i.unit
    except:
        pass
    context = {
        'item': item,
        'total_amount': total_amount,
        'total_unit': total_unit,
    }
    return render(request, 'item_detail.html', context)


@login_required
def bill_create(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.POST:
        formset = item_formset(request.POST, prefix='_itemcount_')
        bill_form = BillForm(request.POST)
        if formset.is_valid() and bill_form.is_valid():
            bill = bill_form.save(commit=False)
            bill.patient = patient
            bill.save()
            for form in formset:
                print(form.cleaned_data.get('item'))
                if form.cleaned_data.get('item') is not None:
                    item_count = form.save(commit=False)
                    print("Item Commit Flase")
                    item_count.bill = bill
                    print("Item Bill Flase")
                    item_count.save()
                    # Item Charges Calculation
                    charges_item = ItemCount.objects.filter(bill=bill)
                    charge_amount = 0
                    for item in  charges_item:
                        charge_amount+=item.amount()
                    bill.charges = charge_amount
                    bill.save()
            return redirect('bnh:bill-pdf', pk=bill.id)
    formset = item_formset(prefix='_itemcount_')
    bill_form = BillForm()
    context = {
        'formset': formset,
        'bill_form':bill_form
    }
    return render(request, 'partials/inline_form.html', context)


# @login_required
# def bill_create(request, pk):
#     patient = get_object_or_404(Patient, id=pk)
#     form = BillForm()
#     if request.POST:
#         form = BillForm(request.POST)
#         if form.is_valid():
#             bill = form.save(commit=False)
#             bill.patient = patient
#             bill.save()
#             service_charge = bill.calculate_amount() * 0.20
#             bill.serv_charge = round(service_charge,2)
#             bill.save()
            

#             return redirect('bnh:home')
#     return render(request, 'partials/create_bill.html', {'form':form})

@login_required
def bill_list(request,pk):
    patient = get_object_or_404(Patient, id=pk)
    bill_list = Bill.objects.filter(patient=patient)
    context = {
        'bill_list': bill_list,
        'patient': patient
    }
    return render(request, 'bill.html', context)

@login_required
def bill_payment(request, pk):
    bill = get_object_or_404(Bill, id=pk)
    if request.POST:
        form = BillPaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.bill = bill
            payment.save()
            bill.paid +=payment.paid_amount
            bill.save()
            return redirect('bnh:bill-list', pk=bill.patient.id)
    context = {
        'form': BillPaymentForm(),
        'bill':bill
    }
    return render(request, 'partials/bill_payment.html', context)


def bill_pdf(request, pk):
    bill_instance = get_object_or_404(Bill, pk=pk)
    item_list = ItemCount.objects.filter(bill=bill_instance)

    # Pass the field information to the template
    context = {
        'bill': bill_instance,
        'item_list':item_list
    }
    return render(request, 'invoice.html', context)

def get_price(request, pk):
    item = Item.objects.get(pk=pk).rate
    return JsonResponse({'price':item})

def summary(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Default values or validation for start_date and end_date
    if not start_date or not end_date:
        # Provide default values or handle the error as needed
        start_date = '2023-01-01'
        end_date = '2023-12-31'

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Filter the BillPayment instances between the specified date range
    filtered_payments = BillPayment.objects.filter(
        Q(payment_date__gte=start_date) & Q(payment_date__lte=end_date)
    )
    total = 0
    if filtered_payments:
        for filter in filtered_payments:
            total += filter.paid_amount

    context = {
        'filtered_payments': filtered_payments,
        'total': total,
        'start_date':request.GET.get('start_date'),
        'end_date':request.GET.get('end_date')
    }

    # Pass the filtered_payments to the template
    return render(request, 'summary.html', context)