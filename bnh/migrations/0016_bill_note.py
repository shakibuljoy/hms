# Generated by Django 5.0 on 2024-01-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0015_bill_discounted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
