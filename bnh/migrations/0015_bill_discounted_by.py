# Generated by Django 5.0 on 2024-01-30 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0014_remove_patient_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='discounted_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
