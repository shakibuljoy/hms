# Generated by Django 5.0 on 2024-01-29 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0013_alter_bill_serv_charge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='district',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='police_station',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='post',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='village',
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default='Chattogram', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='billpayment',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ref_bill', to='bnh.bill'),
        ),
        migrations.AlterField(
            model_name='billpayment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]