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
        fields = '__all__'
        exclude = ['patient', 'serv_charge', 'vat']

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'registration_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'physician_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'consultant_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'assistant_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'dressing': forms.NumberInput(attrs={'class': 'form-control'}),
            'oxigen': forms.NumberInput(attrs={'class': 'form-control'}),
            'nebulization': forms.NumberInput(attrs={'class': 'form-control'}),
            'iv_canula': forms.NumberInput(attrs={'class': 'form-control'}),
            'cbg': forms.NumberInput(attrs={'class': 'form-control'}),
            'ecg': forms.NumberInput(attrs={'class': 'form-control'}),
            'catheter': forms.NumberInput(attrs={'class': 'form-control'}),
            'enema': forms.NumberInput(attrs={'class': 'form-control'}),
            'opc': forms.NumberInput(attrs={'class': 'form-control'}),
            'ot': forms.NumberInput(attrs={'class': 'form-control'}),
            'delivary_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'pathology': forms.NumberInput(attrs={'class': 'form-control'}),
            'observation_3hrs': forms.NumberInput(attrs={'class': 'form-control'}),
            'observation_5hrs': forms.NumberInput(attrs={'class': 'form-control'}),
            'ryles_tube': forms.NumberInput(attrs={'class': 'form-control'}),
            'suction': forms.NumberInput(attrs={'class': 'form-control'}),
            'phototherapy': forms.NumberInput(attrs={'class': 'form-control'}),
            'serv_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'vat': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BillPaymentForm(forms.ModelForm):
    class Meta:
        model = BillPayment
        fields = ['paid_amount']
        widgets = {
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
