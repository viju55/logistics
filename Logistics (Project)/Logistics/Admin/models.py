from django.db import models

# class Category(models.Model):
#     Name = models.CharField(max_length=200, db_index= True)
#     slug = models.SlugField(max_length=200, db_index= True, unique= True)
#
#     class Meta:
#         ordering = ("Name",)
#         verbose_name = "category"
#         verbose_name_plural = "categories"
#
#     def __str__(self):
#         return self.Name
#
# class Product(models.Model):
#     Category = models.ForeignKey(Category, related_name="products", on_delete=False)
#     Name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     Image = models.ImageField(upload_to = "products/%y/%m/%d",blank=True)
#     Description = models.TextField(blank=True)
#     Price = models.IntegerField()
#     Stock = models.PositiveIntegerField()
#     Available = models.BooleanField(default=True)
#     Created = models.DateTimeField(auto_now_add=True)
#     Updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ("-Created",)
#         index_together = (("id","slug"),)
#
#
#     def __str__(self):
#         return self.Name

# class Booking(models.Model):
#     Type_of_transport = models.CharField(max_length=200, db_index=True)
#     Company_name = models.CharField(max_length=200)
#     Name = models.CharField(max_length=20)
#     Telephone_no = models.IntegerField()
#     Email_id = models.EmailField()
#     Country = models.CharField(max_length=10)
#     City = models.CharField(max_length=10)
#     Address = models.CharField(max_length=200)
#
#     class Meta:
#         ordering = ("Name")
#
#     def __str__(self):
#         return self.Name
from django.db.models import CharField


class BOOK(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    No_of_Boxes = models.CharField(max_length=20)
    capacity = models.IntegerField()

    # Date = models.DateTimeField()

    def __str__(self):
        return self.first_name


