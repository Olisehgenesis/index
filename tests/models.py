from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#user
class User(models.Model):
    Email = models.EmailField(max_length=40 , unique=True)
    password = models.CharField(max_length=20)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    School = models.CharField(max_length=30)
    User_Type = models.CharField(max_length=30)
#papers
class Paper(models.Model):
    Email = models.EmailField(max_length=40 , unique=True)
    Test_Title = models.CharField(max_length=200)
    Test_Description = models.CharField(max_length=400)
    Test_Author =models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    School = models.CharField(max_length=100)
#papers
#objectives
class Objective(models.Model):
    Email = models.EmailField(max_length=40 , unique=True)
    Test_Title = models.CharField(max_length=200)
    question = models.CharField(max_length=2000)
    A = models.CharField(max_length=200, null=True)
    B = models.CharField(max_length=200, null=True)
    C = models.CharField(max_length=200,  null=True)
    D = models.CharField(max_length=200 ,null=True)
class structured(models.Model):
    Email = models.EmailField(max_length=40 , unique=True)
    Test_Title = models.CharField(max_length=200)
    question = models.CharField(max_length=10000, null=True)
    answers = models.CharField(max_length=100000, null=True)

