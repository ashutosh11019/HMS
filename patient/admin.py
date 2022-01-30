from django.contrib import admin
from .models import Patient_Profile

# Register your models here.
@admin.register(Patient_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','First_name','Last_name','dob','contact_no')