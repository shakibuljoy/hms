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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father': forms.TextInput(attrs={'class': 'form-control'}),
            'mother': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'village': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.TextInput(attrs={'class': 'form-control'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = ['name', 'code', 'rate']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = ['serv_charge', 'discount', 'vat', 'paid']

        widgets = {
            'serv_charge': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged()', 'onkeyup': 'amountChanged()'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged()', 'onkeyup': 'amountChanged()'}),
            'vat': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged()', 'onkeyup': 'amountChanged()'}),
            'paid': forms.NumberInput(attrs={'class': 'form-control', 'onchange': 'amountChanged()', 'onkeyup': 'amountChanged()'}),
        }

class BillPaymentForm(forms.ModelForm):
    class Meta:
        model = BillPayment
        fields = ['paid_amount']
        widgets = {
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
