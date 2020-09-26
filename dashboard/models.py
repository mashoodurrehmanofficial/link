from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class CurrentPacket(models.Model):
    grabbedlink = models.URLField(max_length=300, unique=True)
    packetID = models.CharField(max_length=100)
    packetlength = models.IntegerField(default=0,blank=True)
    visited = models.BooleanField(default=False, blank=True)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.packetID