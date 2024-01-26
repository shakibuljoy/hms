from django.db import models

dc_status = [('Active','Active'),
                 ('Busy','Busy'),
                 ('Leave','Leave')
                 ]
gender_ch = [
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
    ]
b_group = [
    ('A+', 'A +'),
    ('A-', 'A -'),
    ('B+', 'B +'),
    ('B-', 'B -'),
    ('AB+', 'AB +'),
    ('AB-', 'AB -'),
    ('O+', 'O +'),
    ('O-', 'O -')
]
admit_type = [
    ('In Door','In Door'),
    ('Out Door','Out Door')
]
class Doctor(models.Model):
    name = models.CharField(max_length=120)
    dc_degree = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=dc_status)
    gender = models.CharField(max_length=50, choices=gender_ch) 
    fees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    patient_type = models.CharField(max_length=50, choices=admit_type)
    name = models.CharField(max_length=120)
    father = models.CharField(max_length=120)
    mother = models.CharField(max_length=120, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=gender_ch)
    village = models.CharField(max_length=120, blank=True, null=True)
    post = models.CharField(max_length=120, blank=True, null=True)
    police_station = models.CharField(max_length=120, blank=True, null=True)
    district = models.CharField(max_length=120, blank=True, null=True)
    ref_by = models.CharField(max_length=120, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    age =  models.IntegerField(default=0)
    mobile = models.CharField(max_length=50)
    bed_no = models.CharField(max_length=50, blank=True, null=True)
    cabin = models.CharField(max_length=50, blank=True, null=True)
    b_group = models.CharField(max_length=50, choices=b_group, blank=True, null=True)
    times_of_visit = models.IntegerField(default=0)
    admit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1020)
    rate = models.DecimalField(default=0, decimal_places=2, max_digits=40)

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    charges = models.DecimalField(default=0, decimal_places=2, max_digits=70)
    serv_charge = models.IntegerField(default=0, verbose_name='Service Charge 20%', blank=True, null=True)
    discount = models.IntegerField(default=0)
    vat = models.IntegerField(default=0, verbose_name='VAT %')
    date_create = models.DateTimeField(auto_now=True)
    paid = models.IntegerField(default=0, verbose_name='Paid Amount')

    def __str__(self):
        return f"{self.id}-{self.patient.name} of {self.patient.doctor}"

    def calculate_amount(self):

        # Gather relevant charges (adjust based on your logic)
        total_charges = round(self.charges,2)

        

        # Format and return the amount (adjust as needed)
        return round(total_charges, 2)  # Round to two decimal places
    
    def grand_total(self):
        return self.calculate_amount()+self.serv_charge-self.discount
    
    def due_amount(self):
        return self.grand_total()-self.paid

class ItemCount(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    unit = models.DecimalField(default=1, decimal_places=2, max_digits=40)

    def __str__(self):
        return self.item.name


    def amount(self):
        return round(self.item.rate * self.unit, 2)

class BillPayment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paid_amount = models.IntegerField(default=0)
    payment_date =  models.DateTimeField(auto_now=True)

    
