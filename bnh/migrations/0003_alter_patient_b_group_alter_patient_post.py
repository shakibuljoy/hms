# Generated by Django 5.0 on 2023-12-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0002_rename_bills_bill_rename_doctors_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='b_group',
            field=models.CharField(blank=True, choices=[('A+', 'A +'), ('A-', 'A -'), ('B+', 'B +'), ('B-', 'B -'), ('AB+', 'AB +'), ('AB-', 'AB -'), ('O+', 'O +'), ('O-', 'O -')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='post',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
