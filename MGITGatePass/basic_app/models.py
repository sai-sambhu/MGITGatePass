from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    #addtional
    profile_pic = models.ImageField(upload_to='profile_pics_students',blank=True,default='default.jpeg')
    
    brances = [
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('EEE', 'EEE'),
        ('CIVIL', 'CIVIL'),
        ('MEC', 'MEC'),
    ]
    
    types=[
           ('Incharge', 'Incharge'),
        ('Student', 'Student'), 
    ]
    roll = models.CharField(blank=False ,unique=True,max_length=10) 
    branch = models.CharField(max_length=5,choices=brances,default="CSE")
    typeof = models.CharField(max_length=10,choices=types,default="Student")
    def __str__(self):
        return self.user.username


class GatepassRequests(models.Model):
      opt = [
        ('Denied', 'Denied'),
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
        ('OutOfColloge', 'OutOfColloge'),
        ('NotRequested', 'NotRequested'),
    ]
    
      roll = models.CharField(blank=True,max_length=10)
      branch =  models.CharField(blank=True,max_length=5)
      status = models.CharField(blank=True,choices=opt,max_length=15,default="NotRequested")
      reason = models.CharField(blank=False,max_length=500) 
      
      def __str__(self):
        return self.roll
class AllGatepassRequests(models.Model):
      opt = [
        ('Denied', 'Denied'),
        ('Requested', 'Requested'),
        ('Approved', 'Approved'),
        ('OutOfColloge', 'OutOfColloge'),
        ('NotRequested', 'NotRequested'),
    ]
    
      roll = models.CharField(blank=True,max_length=10)
      branch =  models.CharField(blank=True,max_length=5)
      status = models.CharField(blank=True,choices=opt,max_length=15,default="NotRequested")
      reason = models.CharField(blank=True,max_length=500) 
      dateTime = models.DateTimeField() 
      def __str__(self):
        return self.roll
            
    
