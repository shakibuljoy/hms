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
    name = models.CharField(max_length=120)
    father = models.CharField(max_length=120)
    mother = models.CharField(max_length=120)
    gender = models.CharField(max_length=50, choices=gender_ch)
    village = models.CharField(max_length=120)
    post = models.CharField(max_length=120, blank=True, null=True)
    police_station = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    ref_by = models.CharField(max_length=120)
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

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    registration_fee = models.IntegerField(default=0)
    rent = models.IntegerField(default=0, verbose_name='General Seat Rent\n/Cabinet')
    physician_fee = models.IntegerField(default=0)
    consultant_fee = models.IntegerField(default=0)
    assistant_charge = models.IntegerField(default=0)
    dressing = models.IntegerField(default=0)
    oxigen = models.IntegerField(default=0)
    nebulization = models.IntegerField(default=0)
    iv_canula = models.IntegerField(default=0, verbose_name='I\n/V Cannula Charge')
    cbg = models.IntegerField(default=0, verbose_name='CBG')
    ecg = models.IntegerField(default=0, verbose_name='ECG')
    catheter = models.IntegerField(default=0)
    enema = models.IntegerField(default=0, verbose_name='Enema Simplex')
    opc = models.IntegerField(default=0, verbose_name='Stomach Wash (OPC)')
    ot = models.IntegerField(default=0, verbose_name='O.T (Mini)')
    delivary_charge = models.IntegerField(default=0)
    pathology = models.IntegerField(default=0)
    observation_3hrs = models.IntegerField(default=0)
    observation_5hrs = models.IntegerField(default=0)
    ryles_tube = models.IntegerField(default=0)
    suction = models.IntegerField(default=0)
    phototherapy = models.IntegerField(default=0)
    serv_charge = models.IntegerField(default=0, verbose_name='Service Charge 20%')
    discount = models.IntegerField(default=0)
    vat = models.IntegerField(default=0, verbose_name='VAT %')
    date_create = models.DateTimeField(auto_now=True)
    paid = models.IntegerField(default=0, verbose_name='Paid Amount')

    def __str__(self):
        return f"{self.patient.name} of {self.patient.doctor}"

    def calculate_amount(self):

        # Gather relevant charges (adjust based on your logic)
        total_charges = (self.registration_fee + self.rent + self.physician_fee + self.consultant_fee + self.assistant_charge
            + self.dressing + self.oxigen + self.nebulization + self.iv_canula + self.cbg + self.ecg + self.catheter
            + self.enema + self.opc + self.ot + self.delivary_charge + self.pathology + self.observation_3hrs
            + self.observation_5hrs + self.ryles_tube + self.suction + self.phototherapy)

        

        # Format and return the amount (adjust as needed)
        return round(total_charges, 2)  # Round to two decimal places
    
    def grand_total(self):
        return self.calculate_amount()+self.serv_charge-self.discount
    
    def due_amount(self):
        return self.grand_total()-self.paid


class BillPayment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paid_amount = models.IntegerField(default=0)
    payment_date =  models.DateTimeField(auto_now=True)

    
