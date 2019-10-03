from django.contrib import admin
# from .models import Tranporter_Details
#
# class Transporter_DetailsAdmin(admin.ModelAdmin):
#     list_display = ["Name", "Age", "Photograph", "Vehicle_Number", "License_Number"]
#
#
# admin.site.register(Tranporter_Details,Transporter_DetailsAdmin)

class TransporterAdmin(admin.ModelAdmin):
    list_display = [' username','email','first_name','last_name',' password']