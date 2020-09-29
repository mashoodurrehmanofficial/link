from .models import *
from django.contrib.auth.models import User
from root.models import *
import time,uuid,requests
from datetime import datetime
import urllib.parse

def bidirectionalvisitregistry(request):
    # => ========================================================================= 
    # => =========================== >>>> COMMMMMER <<<<  ========================
    # => =========================================================================  
    
    link = request.GET['visited_link']
    username = request.GET['username']
    ip = request.GET['ip']
    country = request.GET['country']
    # visiting_time = UserVisitingHistory.objects.get(visited_link=link).visiting_time
    # visiting_time =  datetime.strptime(visiting_time,'%Y-%m-%d %H:%M:%S.%f')
    # difference = (datetime.now() - visiting_time).total_seconds()
    required_user=User.objects.get(username=username)
    required_profile = Profile.objects.get(admin=required_user)
    targetted_link = CurrentPacket.objects.get(grabbedlink=link,admin=required_user)
    
    
    # MAKING RECORD IN HISTORY TABLE
    if targetted_link.visited==False:
        UserVisitingHistory(
            visited_link=link,visiting_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ip=ip,country=country,admin=required_user
        ).save()
    
        targetted_link.visited = True
        # UPDATING COMER
        required_profile.currentpacketitemsremaining=required_profile.currentpacketitemsremaining-1
        required_profile.packetitemsvisited = required_profile.packetitemsvisited+1
        required_profile.reserved_tokens = required_profile.reserved_tokens+1
        required_profile.totalregisteredvisits = required_profile.totalregisteredvisits+1
        targetted_link.save()
        required_profile.save()
        
        # EXTRACTING TARGET PROFILE
        # EXTRACTING TARGET PROFILE
        analyzed_link = urllib.parse.urlsplit(str(targetted_link.grabbedlink))
        analyzed_link = analyzed_link.scheme+"://"+analyzed_link.netloc+analyzed_link.path
        print('==================')
        analyzed_link = UserUrlssRepository.objects.get(submitted_url=analyzed_link)
        target_profile = Profile.objects.get(admin=analyzed_link.admin)
        target_profile.reserved_tokens = target_profile.reserved_tokens-1
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
    