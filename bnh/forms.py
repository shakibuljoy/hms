from django import forms
from django.forms import formset_factory
from .models import Doctor, Patient, Bill, BillPayment, Item, ItemCount

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'dc_degree', 'address', 'status', 'gender', 'fees']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set user-friendly labels for choice fields
        self.fields['status'].label = "Status"
        self.fields['gender'].label = "Gender"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'  # You can specify the fields you want to include if needed

        widgets = {
            'patient_type': forms.Select(attrs={'class': 'form-control', 'onchange':'typeChange(this)'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father': forms.TextInput(attrs={'class': 'form-control'}),
            'mother': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'ref_by': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'bed_no': forms.TextInput(attrs={'class': 'form-control'}),
            'cabin': forms.TextInput(attrs={'class': 'form-control'}),
            'b_group': forms.Select(attrs={'class': 'form-control'}),
            'times_of_visit': forms.NumberInput(attrs={'class': 'form-control'}),
            # 'admit_time': You might not want to include this in the form for user input
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'rate']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ItemAmountForm(forms.ModelForm):
    class Meta:
        model = ItemCount
        fields= [ 'item', 'unit']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control', 'onchange':'itemChange(this)'}),
            'unit': forms.NumberInput(attrs={'class': 'form-control', 'step':1}),
        }

item_formset = formset_factory(ItemAmountForm, extra=2)

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['serv_charge','discounted_by', 'discount', 'vat', 'paid', 'note']

        widgets = {
            'serv_charge': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged(serv_charge=true)', 'onkeyup': 'amountChanged(serv_charge=true)'}),
            'discounted_by': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged(serv_charge=false)', 'onkeyup': 'amountChanged(false)'}),
            'vat': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged(serv_charge=false)', 'onkeyup': 'amountChanged(false)'}),
            'paid': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged(serv_charge=false)', 'onkeyup': 'amountChanged(false)'}),
            'note': forms.Textarea(attrs={'cols':'30', 'rows':'5'}),
        }

class BillPaymentForm(forms.ModelForm):
    class Meta:
        model = BillPayment
        fields = ['paid_amount']
        widgets = {
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
