# Generated by Django 5.0 on 2024-01-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0009_remove_bill_assistant_charge_remove_bill_catheter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='code',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='ok', max_length=1020),
            preserve_default=False,
        ),
    ]
