from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=200)
    contactno = models.CharField(max_length=15)
    emailaddress = models.CharField(max_length=50)
    enquirytext = models.CharField(max_length=500)

class JobSeeker(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=200)
    contactno = models.IntegerField(primary_key=True)
    emailaddress = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    keyskills = models.CharField(max_length=200)
    regdate = models.CharField(max_length=30)

class AdminLogin(models.Model):
    objects = None
    userid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=30)
