from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout  
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from root.models import *
from .models import *
import requests,time,random,uuid
# Create your views here. 



def grabandpostlinks(request):
    return render(request, 'dashboard/grabandpostlinks.html')





# Create your views here.
# INDEX PAGE
 
# DASHBOARD

@login_required(login_url='/login')
def dashboard(request):  
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
        'title':'claimtraffic'
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
        'title':'Dashboard'
    }
    return render(request, 'dashboard/configureurls.html',context)
  

from django.forms.models import model_to_dict
 
# STATISTICS
@login_required(login_url='/login')
def statistics(request):  
    user_profile = Profile.objects.get(admin=request.user)
    user_urls = UserUrlssRepository.objects.filter(admin=request.user).order_by('-id')
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'Dashboard'
    }
    return render(request, 'dashboard/statistics.html',context)
  


def grablinkspacket(request):
    required_profile=Profile.objects.get(admin=request.user)
    if required_profile.current_packet_completed: 
        print("Deleting previous Allocations")
        CurrentPacket.objects.filter(admin=request.user).delete()
        print('Performing link allocation')
        # capacity = request.GET['capacity'] 
        packetID=uuid.uuid4() 
        alloted_links = [x.submitted_url for x in UserUrlssRepository.objects.all()] 
        required_profile=Profile.objects.get(admin=request.user)
        required_profile.current_packet_completed=False
        required_profile.current_packetID=packetID
        required_profile.current_packetlength=len(alloted_links)
        required_profile.save()
        CurrentPacket.objects.bulk_create(
            [CurrentPacket(grabbedlink=x, packetlength=len(alloted_links),packetID=packetID, admin=request.user) for x in alloted_links]
        )
        print('Allocation completed !')
        return JsonResponse({'alloted':True,'alloted_links':alloted_links})
    else:
        return JsonResponse({'alloted':False,'alloted_links':[0]})