from django.db import models
from django.contrib.auth.models import User  
# Create your models here.



class CurrentPacket(models.Model):
    grabbedlink = models.URLField(max_length=300)
    packetID = models.CharField(max_length=100)
    packetlength = models.IntegerField(default=0,blank=True)
    visited = models.BooleanField(default=False, blank=True)
    packet_creation_time = models.IntegerField(default=0,blank=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.admin.username +' '+ self.packetID
    
class ClaimTank(models.Model):
    claimed_link = models.CharField(max_length=300,default='')
    raw_link = models.CharField(max_length=300,default='')
    submittion_time = models.IntegerField(default=0,blank=True)
    tempID = models.CharField(max_length=100,default='',blank=True)
    alloted = models.BooleanField(default=False, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.admin.username +' '+ self.claimed_link


class UserVisitingHistory(models.Model):
    visited_link = models.URLField(max_length=300,blank=True)
    pure_link = models.URLField(max_length=300,blank=True)
    visiting_time = models.IntegerField(default=0,blank=True)
    ip = models.CharField(max_length=20,default='')
    country = models.CharField(max_length=100,default='',blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.admin.username + ' ' + self.visited_link