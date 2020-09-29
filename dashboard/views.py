from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout  
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from root.models import *
from .models import *
import requests,time,random,uuid
from datetime import  datetime
# Create your views here. 


 


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
    total_configured_urls = UserUrlssRepository.objects.filter(admin=request.user).count()  
    # current_packet = CurrentPacket
    context={
        'user_urls':user_urls,
        'user_profile':user_profile,
        'title':'Dashboard',
        'total_configured_urls':total_configured_urls
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
    return JsonResponse({'alloted':True,'alloted_links':alloted_links})
    # else:
    #     return JsonResponse({'alloted':False,'alloted_links':[0]})
    
 
from .bidirectionalvisitregistry import  bidirectionalvisitregistry
def registermyvisit(request): 
    bidirectionalvisitregistry(request)
    return JsonResponse({'data':12})
    