# Generated by Django 5.0 on 2023-12-22 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnh', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bills',
            new_name='Bill',
        ),
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.RenameModel(
            old_name='Patients',
            new_name='Patient',
        ),
    ]