from django.contrib import admin
from .models import *


#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["Name", "slug"]
#     prepopulated_fields = {'slug':("Name",)}
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["Name","slug","Image","Description","Price","Stock","Available","Created","Updated"]
#     list_filter = ["Available","Created","Updated","Category"]
#     list_editable = ["Price","Stock","Available"]
#     prepopulated_fields = {'slug':("Name",)}
#
#
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(Product,ProductAdmin)

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ['Type_of_transport', 'Company_name', ' Name', 'Telephone_no', ' Email_id', 'Country', 'City',
#                     ' Address']
# admin.site.register(Booking, BookingAdmin)

class BOOKAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','contact','No_of_Boxes','capacity']
admin.site.register(BOOK,BOOKAdmin)
