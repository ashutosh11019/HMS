from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','subject','email','date')



#python manage.py makemigrations
#python manage.py migrate
