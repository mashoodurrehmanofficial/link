from django.core.exceptions import  ObjectDoesNotExist
from .models import *
from django.contrib.auth.models import User
from root.models import *
import time,uuid,requests 
import urllib.parse,math,datetime
from django.http import JsonResponse

def claimTANKsecurity(request):
    claimed_link = request.GET['claimed_link'].split(',')
    required_profile = Profile.objects.get(admin=request.user) 
    # IN CASE OF ZERO BALANCE 
    if required_profile.remaining_balance<1:
        print(required_profile.remaining_balance)
        return JsonResponse({'status':'zerobalance'})
    # IN CASE OF LESS BALANCE
    if len(claimed_link)>required_profile.remaining_balance:
        claimed_link = claimed_link[:int(required_profile.remaining_balance)]
        return JsonResponse({'data':'Warning !'}) 
    
    
    try:last = ClaimTank.objects.filter(admin=request.user).order_by('-id')[0].submittion_time
    except:last=0 
    now = int(datetime.datetime.today().timestamp())
    difference = (now-last)/60
    def diffinterval():
        if difference<1:
            print('condnition3')   
            return [False, 'durationerror']
        elif difference>=2:
            print('condnition4')   
            return [True, 'pass']
        else:
            return [False, 'durationerror']
    
    # GETTING LATEST POPULATION 
    def getlatestclaimations():
        all_items = ClaimTank.objects.all().order_by('-id')
        current_user_items = ClaimTank.objects.filter(admin=request.user)
        print(current_user_items)
        print('__________')
        all30p1 = int( (len(all_items)*30)/100)
        all30p2 = round((all30p1*30)/100 )
        print('_____',all30p2)
        all30pitems = [x.admin for x in all_items[:all30p1]].count(request.user) 
        
        # print(all30pitems) 
        # print(all30p1)
        # print(all30p2)
        # print(all20p)
        
        # TEMPORARY SETTINGS
        if len(current_user_items)<1 and len(claimed_link)<=all30p2:
            print('NEW___COMER')
            return [True, 'pass']
        elif len(all_items)<=10 and len(claimed_link)<=6 and len(current_user_items.order_by('-id'))<=5: 
            print('condnition1')   
            return [True, 'pass']
        elif len(all_items)<=10 and len(claimed_link)>3 and len(current_user_items.order_by('-id'))<=5:
            print('condnition2')   
            return [False, 'emptytanklinitedlength']
        elif all30p1==all30pitems:
            print('condnition3')   
            return [False, 'later']
        # elif all30pitems>all30p2:
        #     return [False, 'later']
        elif math.isclose(all30pitems,all30p2, abs_tol=2):
            print('approximate decision !')
            return [True, 'pass']
        else:
            return [False, 'error']
            
         
        
    
    # IMPLEMENTING TIME DURATION FOR 
    result = getlatestclaimations()
    if result[0]:
        print('success')
        print(difference)  
        ClaimTank.objects.bulk_create(
            [ClaimTank(claimed_link=x,submittion_time=int(datetime.datetime.today().timestamp()),admin=request.user) for x in claimed_link]
        )  
        required_profile.totalclaimedtraffic=required_profile.totalclaimedtraffic+len(claimed_link)
        required_profile.remaining_balance = required_profile.remaining_balance-len(claimed_link)
        required_profile.save()
        return JsonResponse({'status':result[1],'remaining_balance':required_profile.remaining_balance})
    else:
        print(result[1])
        print('error')
        print(difference)
        return JsonResponse({'status':result[1]})    
    