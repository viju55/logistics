from django.db import models

# class Tranporter_Details(models.Model):
#     Name = models.CharField(max_length=50)
#     Age = models.IntegerField()
#     Photograph = models.ImageField(upload_to="transporter/%y/%m/%d",blank=True)
#     Vehicle_Number = models.CharField(max_length=20)
#     License_Number = models.CharField(max_length=20)


class Transporter(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.first_name








