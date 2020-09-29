from .models import *
from django.contrib.auth.models import User
from root.models import *
import time,uuid,requests
from datetime import datetime
import urllib.parse

exceeding_limit={'5':1,'10':2,'15':2,'20':2,'25':3,'30':3,'35':3,'40':3,'45':4,'50':4}
 
def linkpackallocation(request):
    required_profile=Profile.objects.get(admin=request.user)
    if required_profile.current_packet_completed: 
        print("Deleting previous Allocations")
        CurrentPacket.objects.filter(admin=request.user).delete()
        print('Performing link allocation')
        capacity = int(request.GET['capacity'] )
        packetID=uuid.uuid4() 
        packet_creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Grabbing all Links
        alloted_links = UserUrlssRepository.objects.all()
        # Restricting Current USER
        alloted_links = alloted_links.exclude(admin=request.user)
        alloted_links = [x.submitted_url for x in alloted_links]
        # Getting exceeding Limit 
        max_repeating_links = exceeding_limit[f'{capacity}'] 
        
        
        
        # IMPLEMENTING Restriction of MAX REDUNDANCY
        def generate_purified_links():
            total_websites = Profile.objects.exclude(website='').count()
            # Getting exceeding Limit 
            max_repeating_links = exceeding_limit[f'{capacity}'] 
            # 1 NO. of WEBSITES <= CAPACITY
            if int(total_websites)>=capacity:
                max_repeating_links=1
            # 2 CONDITION MAX REDUNDANCY
            group_by_domain = list(set([urllib.parse.urlsplit(x).netloc  for x in alloted_links])) 
            for x in group_by_domain:
                group_by_domain[group_by_domain.index(x)]=[y for y in alloted_links if x in str(y)]
            purified_links = []
            for z in group_by_domain: 
                purified_links=purified_links+z[:max_repeating_links]
            return purified_links 
        
        
        
        # Specifying Capacity
        alloted_links = generate_purified_links()[:capacity]
        # Converting to LIST 
        CurrentPacket.objects.bulk_create(
            [CurrentPacket(grabbedlink=str(x)+f'?username={request.user.username}',packet_creation_time=packet_creation_time, packetlength=len(alloted_links),packetID=packetID, admin=request.user) for x in alloted_links]
        )
        required_profile.current_packetID=packetID
        required_profile.current_packetlength=len(alloted_links)
        required_profile.currentpacketitemsremaining=len(alloted_links)
        required_profile.packetitemsvisited=0
        required_profile.current_packet_completed=False
        required_profile.packet_creation_time = packet_creation_time
        required_profile.save()
        print('Allocation completed !')
    return alloted_links