from django.db import models

# Create your models here.


class STUDENTS(models.Model):
    pic = models.ImageField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=6)
    nationality = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    lga_origin = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255)
    jamb_number = models.CharField(max_length=10)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=500)
    level = models.CharField(max_length=4)
    matric_number = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    parent_name = models.CharField(max_length=255)
    parent_email = models.EmailField(max_length=254)
    parent_phone = models.CharField(max_length=11)
    date_of_registration = models.DateField(auto_now=False, auto_now_add=False)


class STAFF(models.Model):
    pic = models.ImageField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=6)
    nationality = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    lga_origin = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    date_of_registration = models.DateField(auto_now=False, auto_now_add=False)
