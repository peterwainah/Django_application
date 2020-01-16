from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    

def __str__(self):
  return self.user.username

class ScholarshipApplication(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)  
    email=models.CharField(max_length=40) 
    Birth_certificate = models.ImageField(upload_to='profile_pics',blank=True)
    National_id = models.ImageField(upload_to='profile_pics',blank=True)
class SchoolInformation(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    academic_level = models.CharField(max_length=30)  
    expected_year_of_completion=models.CharField(max_length=40)
    
class JustInformation(models.Model):
   Reasons_to_be_sponsored = models.TextField(max_length=400)
   Recomendation_letter = models.ImageField(upload_to='profile_pics',blank=True)
