from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout  
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from root.models import *
from .models import *
import requests,time,random,uuid,datetime

# Create your views here. 


def packetcompletionanamoly(request):
    required_profile = Profile.objects.get(admin=request.user)
    if required_profile.currentpacketitemsremaining==0:
        required_profile.current_packet_completed=True
        required_profile.save()
    if required_profile.current_packetlength==required_profile.packetitemsvisited:
        required_profile.current_packet_completed=True
        required_profile.save()
    else:pass


# Create your views here.
# INDEX PAGE
 
# DASHBOARD

@login_required(login_url='/login')
def dashboard(request):  
    packetcompletionanamoly(request)
    user_profile = Profile.objects.get(admin=request.user)
    alloted_links = CurrentPacket.objects.filter(admin=request.user) 
    counting = len(alloted_links)
    context={ 
        'user_profile':user_profile,
        'alloted_links':alloted_links,
        'counting':counting,
        'title':'Dashboard'
    } 
    return render(request, 'dashboard/grablinks.html',context)


@login_required(login_url='/login')
def claimtraffic(request):  
    user_profile = Profile.objects.get(admin=request.user)
    user_urls = UserUrlssRepository.objects.filter(admin=request.user).order_by('-id')
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'ClaimTraffic'
    }
    return render(request, 'dashboard/claimtraffic.html',context)




# CONFIGUREYRLS
@login_required(login_url='/login')
def configureurls(request):  
    user_profile = Profile.objects.get(admin=request.user)
    user_urls = UserUrlssRepository.objects.filter(admin=request.user).order_by('-id')
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'Configure URLs'
    }
    return render(request, 'dashboard/configureurls.html',context)
  

from django.forms.models import model_to_dict
 
# STATISTICS
@login_required(login_url='/login')
def statistics(request):  
    packetcompletionanamoly(request)
    user_profile = Profile.objects.get(admin=request.user)
    user_urls = UserUrlssRepository.objects.filter(admin=request.user).order_by('-id')
    total_configured_urls = UserUrlssRepository.objects.filter(admin=request.user).count() 
    packetcreationtime = datetime.datetime.fromtimestamp(user_profile.packet_creation_time)
    linksinqueue=ClaimTank.objects.filter(admin=request.user).count()
    # current_packet = CurrentPacket
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'Statistics',
        'total_configured_urls':total_configured_urls,
        'packetcreationtime': str(packetcreationtime),
        'linksinqueue':linksinqueue
    }
    return render(request, 'dashboard/statistics.html',context)
  

# testurls
@login_required(login_url='/login')
def testurls(request):  
    user_profile = Profile.objects.get(admin=request.user)
    user_urls = UserUrlssRepository.objects.filter(admin=request.user).order_by('-id')
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'Dashboard'
    }
    return render(request, 'dashboard/testurls.html',context)
  



from .linkpacketallocation import linkpackallocation
def grablinkspacket(request):
    alloted_links = linkpackallocation(request)
    return JsonResponse({'alloted':alloted_links[0],'alloted_links':alloted_links[1],'extra':alloted_links[2]})
    
     
    
from .bidirectionalvisitregistry import  bidirectionalvisitregistry
def registermyvisit(request): 
    try:
        bidirectionalvisitregistry(request)
        return JsonResponse({'status':'registered'})
    except ObjectDoesNotExist:
        return JsonResponse({'status':'packetexpired'})
        
    
    
    
from .claimTANKsecurity import claimTANKsecurity
def claimTank(request):  
    return claimTANKsecurity(request)
    