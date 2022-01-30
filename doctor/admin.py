from django.contrib import admin

# Register your models here.
from .models import Doctor_Profile

# Register your models here.
@admin.register(Doctor_Profile)
class Doctor_ProfileAdmin(admin.ModelAdmin):
    list_display=('id','First_name','Last_name','dob','contact_no')