from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.contrib.auth.models import User
from root.models import *
import time,uuid,requests 
import urllib.parse
import datetime

def bidirectionalvisitregistry(request):
    # => ========================================================================= 
    # => =========================== >>>> COMMMMMER <<<<  ========================
    # => =========================================================================  
    
    link = request.GET['visited_link']
    username = request.GET['username']
    ip = request.GET['ip']
    print(ip)
    country = request.GET['country'] 
    required_user=User.objects.get(username=username)
    required_profile = Profile.objects.get(admin=required_user)
    targetted_link = CurrentPacket.objects.get(grabbedlink=link,admin=required_user)
    
    print(targetted_link.packetID)
    # MAKING RECORD IN HISTORY TABLE
    if targetted_link.visited==False:
        analyzed_link = urllib.parse.urlsplit(str(targetted_link.grabbedlink))
        analyzed_link = analyzed_link.scheme+"://"+analyzed_link.netloc+analyzed_link.path
        UserVisitingHistory(
            visited_link=link,visiting_time=int(datetime.datetime.today().timestamp()),
            ip=ip,country=country,admin=required_user,pure_link=analyzed_link
        ).save()
    
        
        # UPDATING COMER
        required_profile.currentpacketitemsremaining=required_profile.currentpacketitemsremaining-1
        required_profile.packetitemsvisited = required_profile.packetitemsvisited+1
        required_profile.reserved_tokens = required_profile.reserved_tokens+1
        required_profile.remaining_balance = required_profile.remaining_balance+1
        required_profile.totalregisteredvisits = required_profile.totalregisteredvisits+1
        required_profile.last_visit_time = int(datetime.datetime.today().timestamp())
        targetted_link.visited = True
        targetted_link.save()
        required_profile.save()
        
        # EXTRACTING TARGET PROFILE
        # EXTRACTING TARGET PROFILE
        analyzed_link = urllib.parse.urlsplit(str(targetted_link.grabbedlink))
        analyzed_link = analyzed_link.scheme+"://"+analyzed_link.netloc+analyzed_link.path
        # print('==================')
        analyzed_link = ClaimTank.objects.get(claimed_link=analyzed_link,tempID=required_profile.current_packetID,alloted=True)
        print(analyzed_link.tempID)
        target_profile = Profile.objects.get(admin=analyzed_link.admin)
        analyzed_link.delete()
        target_profile.reserved_tokens = target_profile.reserved_tokens-1
        target_profile.totaltrafficreturnedback=target_profile.totaltrafficreturnedback+1
        target_profile.save()
        
        # CHECKING FOR LAST ITEM TO MAKE CURRENT PACKET COMPLETED
        if required_profile.currentpacketitemsremaining<=0:
            required_profile.current_packet_completed=True
            required_profile.save()
            print(required_profile.current_packetlength)
    
        print('________________')
        print(targetted_link)
        print(ip)
        print(country, )
        print( username)
        print(link)
        print('________________')
        
    # => ========================================================================= 
    # => ============================= >>>> target <<<<  =========================
    # => =========================================================================  
    