# Generated by Django 3.2.9 on 2022-01-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20220130_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_profile',
            name='verify',
            field=models.BooleanField(default=True),
        ),
    ]
