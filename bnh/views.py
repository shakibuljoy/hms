from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm, PatientForm, BillForm, BillPaymentForm
from .models import Doctor, Patient, Bill


def home(request):
    patient = Patient.objects.all()
    context = {
        'patient_list': patient
    }
    return render(request, 'home.html', context)

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
            return redirect('bnh:home')
    return render(request, 'partials/create_patient.html', {'form':form})

@login_required
def bill_create(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    form = BillForm()
    if request.POST:
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill.patient = patient
            bill.save()
            service_charge = bill.calculate_amount() * 0.20
            bill.serv_charge = round(service_charge,2)
            bill.save()
            

            return redirect('bnh:home')
    return render(request, 'partials/create_bill.html', {'form':form})

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

    # Pass the field information to the template
    context = {
        'bill': bill_instance,
    }
    return render(request, 'invoice.html', context)
