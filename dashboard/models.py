from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime
# Create your models here.



class CurrentPacket(models.Model):
    grabbedlink = models.URLField(max_length=300)
    packetID = models.CharField(max_length=100)
    packetlength = models.IntegerField(default=0,blank=True)
    visited = models.BooleanField(default=False, blank=True)
    packet_creation_time = models.CharField(max_length=100,default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.packetID
    
class UserVisitingHistory(models.Model):
    visited_link = models.URLField(max_length=300,blank=True)
    visiting_time = models.CharField(max_length=100,default=datetime.now())
    ip = models.GenericIPAddressField(default='')
    country = models.CharField(max_length=100,default='',blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.admin.username + ' ' + self.visited_link