# Generated by Django 3.2.9 on 2022-01-30 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_profile',
            old_name='fn',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='patient_profile',
            old_name='ln',
            new_name='Last_name',
        ),
    ]
