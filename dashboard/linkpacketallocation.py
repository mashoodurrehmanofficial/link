from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
from root.models import *
import time,uuid,requests,datetime
import urllib.parse
RESTRICTING_D0MAIN_TIMING=1800
PACKET_EXPIRATION_TIMING=600
UNTOUCHED_PACKET_EXPIRATION_TIMING=180


exceeding_limit={'5':1,'10':2,'15':2,'20':2,'25':2,'30':3,'35':3,'40':3,'45':4,'50':4}
 
def linkpackallocation(request):
    # (613, 'https://materializecss.com/pushpin.html?username=khan', '7bf08948-7f46-4f30-b6e2-a093463287de', 8, False, 1601642583, 29)
    
     # DELETING UN-TOUCHED PACKETS
    def delete_untouched_packets():
        # WANTED PROFILES
        packet_expiration_time = int(datetime.datetime.today().timestamp())-UNTOUCHED_PACKET_EXPIRATION_TIMING
        wanted_profiles = Profile.objects.exclude(last_visit_time__gte=packet_expiration_time)
        for wanted in wanted_profiles:
            wanted.current_packetlength=wanted.packetitemsvisited
            wanted.current_packet_completed=True
            wanted.save()
            
            CurrentPacket.objects.filter(packetID=wanted.current_packetID,visited=False).delete()
            ClaimTank.objects.filter(alloted=True,tempID=wanted.current_packetID).update(
                alloted=False,raw_link='',tempID='',
            )
            
        print(wanted_profiles)
    delete_untouched_packets()
    
    
    
    
    
    
    
    
    
    # DELETING EXPIRED PACKETS
    def delete_exired_packets():
        packet_expiration_time = int(datetime.datetime.today().timestamp())-PACKET_EXPIRATION_TIMING
        TARGET_PACKETS = CurrentPacket.objects.filter(packet_creation_time__lte=packet_expiration_time,visited=False)
        TARGET_ADMINS = [x.admin for x in TARGET_PACKETS]
        TARGET_PROFILES = Profile.objects.filter(admin__in=TARGET_ADMINS) 
        for x in TARGET_PACKETS.values_list():
            print('__________deleted',x)
            packetitem = CurrentPacket.objects.filter(grabbedlink=x[1],packetID=x[2])
            packetitem.delete()
            stucked_link = ClaimTank.objects.get(raw_link=x[1],tempID=x[2])
            stucked_link.alloted=False
            stucked_link.raw_link=''
            stucked_link.tempID=''
            stucked_link.save() 
            required_profile = Profile.objects.get(current_packetID=x[2])
            required_profile.current_packetlength=required_profile.packetitemsvisited
            required_profile.current_packet_completed=True
            required_profile.save()
    delete_exired_packets()
    
    
    
    
    
    required_profile=Profile.objects.get(admin=request.user)
    if required_profile.current_packet_completed: 
        print("Deleting previous Allocations")
        CurrentPacket.objects.filter(admin=request.user).delete()
        print('Performing link allocation')
        capacity = int(request.GET['capacity'] )
        packetID=uuid.uuid4() 
        packet_creation_time  = int(datetime.datetime.today().timestamp())
        
        # 1. Grabbing all Links
        # Profile.objects.all().update(current_packet_completed=True)
        # ClaimTank.objects.filter(alloted=True).update(alloted=False) 
        alloted_links = ClaimTank.objects.all().exclude(alloted=True)
        # 2. Restricting Current USER
        alloted_links = alloted_links.exclude(admin=request.user)
        alloted_links = [x.claimed_link for x in alloted_links]
        # 3. RESTRICTING BALANCE >=20
        if required_profile.remaining_balance>=15:
            return [False,'balanceisextra','']
        
        # Getting exceeding Limit 
        max_repeating_links = exceeding_limit[f'{capacity}'] 
        
        
        # 4. IF TANK IS EMPTY THEN DON'T CREATE PACKET
        if len(alloted_links) <1:
            return [False,"emptyrepository",'']
        # IMPLEMENTING Restriction of MAX REDUNDANCY
        def generate_purified_links():
            total_websites = Profile.objects.exclude(website='').count()
            # Getting exceeding Limit 
            max_repeating_links = exceeding_limit[f'{capacity}'] 
            # 5. NO. of WEBSITES >= CAPACITY
            if int(total_websites)>=capacity:
                max_repeating_links=1
            # 6. RESTRICTING HISTORY DOMAINS
            now = int(datetime.datetime.today().timestamp())# SECS 
            print('______________')
            recentsite = UserVisitingHistory.objects.filter(admin=required_profile.admin)
            recentsite=recentsite.filter(visiting_time__gte=now-RESTRICTING_D0MAIN_TIMING).order_by('-id')
            recentsite=[x.pure_link for x in recentsite]
            restricteddomain = list(set([urllib.parse.urlsplit(x).netloc  for x in recentsite]))  
            fake=[]
            for x in alloted_links:
                for y in restricteddomain:
                    if str(y) in str(x):
                        fake.append(x)
            purealloted_links = set(set(alloted_links)-set(fake))
            print(purealloted_links)
            print('______________')
            print(alloted_links)
            
            
            # 7. CONDITION MAX REDUNDANCY
            group_by_domain = list(set([urllib.parse.urlsplit(x).netloc  for x in purealloted_links])) 
            for x in group_by_domain:
                group_by_domain[group_by_domain.index(x)]=[y for y in purealloted_links if x in str(y)]
            purified_links = []
            for z in group_by_domain: 
                purified_links=purified_links+z[:max_repeating_links]
            return purified_links 
        
        
        
        
        # # Specifying Capacity
        purealloted_links = list(set(generate_purified_links()[:capacity]))
        listbeforenameadd = purealloted_links
        if len(purealloted_links)==0:
            return [False,"grablimitexceed",'']
        print(listbeforenameadd) 
        # Converting to LIST 
        CurrentPacket.objects.bulk_create(
            
            [CurrentPacket(grabbedlink=str(x)+f'?username={request.user.username}',packet_creation_time=packet_creation_time, packetlength=len(purealloted_links),packetID=packetID, admin=request.user) for x in purealloted_links]
        )
        required_profile.current_packetID=packetID
        required_profile.current_packetlength=len(purealloted_links)
        required_profile.currentpacketitemsremaining=len(purealloted_links)
        required_profile.packetitemsvisited=0
        required_profile.current_packet_completed=False
        required_profile.packet_creation_time = packet_creation_time
        required_profile.last_visit_time = packet_creation_time
        required_profile.save()
        print('Allocation completed !')
        purealloted_links = [x.grabbedlink for x in CurrentPacket.objects.filter(packetID=packetID)]
        
        # UPDATING ALLOTED STATUS 
        for x in listbeforenameadd:
            located = ClaimTank.objects.filter(claimed_link=x).first()
            located.alloted=True
            located.raw_link = str(located.claimed_link)+f'?username={request.user.username}'
            located.tempID=packetID
            located.save()
             
        
    # return [False,'',''] 
    if len(purealloted_links)<capacity:
        return [True,purealloted_links,'lesslinks']
    else:
        return [True,purealloted_links,'']