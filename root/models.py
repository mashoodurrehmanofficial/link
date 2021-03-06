from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  

# Create your models here.
class Profile(models.Model):
    email_verified = models.BooleanField(default=True)
    userid = models.CharField(max_length=100,default='',blank=True)
    website = models.CharField(max_length=100, default='',blank=True) 
    gender = models.CharField(max_length=6,default='',blank=True)  
    admin = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
    current_packetID = models.CharField(max_length=100, blank=True)
    current_packetlength = models.IntegerField(default=0,blank=True)
    currentpacketitemsremaining = models.IntegerField(default=0,blank=True)
    packetitemsvisited = models.IntegerField(default=0,blank=True)
    reserved_tokens = models.IntegerField(default=0,blank=True)
    remaining_balance = models.IntegerField(default=0,blank=True)
    
    totalregisteredvisits = models.IntegerField(default=0,blank=True)
    totalclaimedtraffic = models.IntegerField(default=0,blank=True)
    totaltrafficreturnedback = models.IntegerField(default=0,blank=True)
    
    current_packet_completed = models.BooleanField(default=True)
    packet_creation_time = models.IntegerField(default=0)
    last_visit_time = models.IntegerField(default=0)
    
    def __str__(self):
        return self.admin.username +' _____'+ self.website
    
    
@receiver(post_save, sender=User)
def create_profile(sender,instance,**kwargs):
    Profile.objects.get_or_create(admin=instance)
    
class EmailVerification(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    codesent = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    
class UserUrlssRepository(models.Model):
    title = models.CharField(max_length=300)
    submitted_url = models.URLField(max_length=300, unique=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.admin.username + ' ' +self.submitted_url