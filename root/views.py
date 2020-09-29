from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout  
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import *
import requests,time,random,uuid
import urllib.parse,requests,json
# Create your views here.
# INDEX PAGE
def index(request):
    return render(request, 'root/index.html')

# REGISTER PAGE
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']        
        password = request.POST['password']
        new_user = User.objects.create_user(username=name,password=password,email=email)
        new_user.save()
        return redirect('login')
    else:
        return render(request, 'root/register.html')

# LOGIN PAGE
def user_login(request): 
    if request.user.is_authenticated:
      return  redirect('/')
    if request.method == 'POST':
      username = request.POST['name']
      password = request.POST['password']
    #   try:
    #     captcha_token=request.POST.get("g-recaptcha-response")
    #     cap_url="https://www.google.com/recaptcha/api/siteverify"
    #     cap_secret="6LedltEZAAAAAChfcWQ1cPIQS1OM0iUm7YFDPsjS"
    #     cap_data={"secret":cap_secret,"response":captcha_token}
    #     cap_server_response=requests.post(url=cap_url,data=cap_data)
    #     cap_json=json.loads(cap_server_response.text)
    #     print(cap_json)
    #     if cap_json['success']==False:
    #         return HttpResponseRedirect("/")
    #   except:
    #       return redirect('login')
    
    
      user = authenticate(username=username, password=password)
      if user is not None: 
        login(request, user)
        return redirect('dashboard')
      else:
        return render(request, 'root/login.html', {'user': False})
    else:
      return render(request, 'root/login.html', {'user': False})

# DASHBOARD
 


# LOGOUT
def logout_user(request):
    logout(request) 
    return redirect('login') 


def sendemailcode(request):
    import smtplib, ssl,uuid
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    print(request.user.email)
    code=uuid.uuid4()
    try:EmailVerification(email=request.user.email,codesent=code).save()
    except:
        required_email = EmailVerification.objects.get(email=request.user.email)
        required_email.codesent=code
        required_email.save()
    try:
        sender_email = "mashoodurrehmanofficial@gmail.com"
        receiver_email = str(request.user.email)
        password = "play@715"

        message = MIMEMultipart("alternative")
        message["Subject"] = "EmailVerification :)"
        message["From"] = sender_email
        message["To"] = receiver_email
        html = f"""\
        <html>
        <body>
            <p>Hi,<br> 
            {code}
            </p>
        </body>
        </html>
        """ 
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(html, "html") 
        message.attach(part1) 
        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return JsonResponse({"status":1})
    except :
        return JsonResponse({"status":0})

def verifysentcode(request):
    required_email = EmailVerification.objects.get(email=request.user.email)
    # if required_email.codesent!=1: 
    if required_email.codesent==request.GET['emailcode']: 
        reqired_profile = Profile.objects.get(admin=request.user)
        reqired_profile.email_verified=True
        reqired_profile.save()
        required_email.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})




def verifylink(request):
    link=request.GET['link'] 
    try:
        status_code=requests.get(link).status_code
    except:status_code=0
    return JsonResponse({"status":status_code}) 

def submitID(request): 
    website=request.GET['website'] 
    user_profile = Profile.objects.get(admin=request.user)
    user_profile.userid = str(website).replace('.','')
    user_profile.website = website
    user_profile.save()
    
    return redirect('dashboard') 

def sessioncompleted(request):
    print(request.GET['ip'])
    print(request.GET['userid'])
    print(request.GET['link']) 
    return JsonResponse({"q":2}) 

def personalinfo(request): 
    user_profile = Profile.objects.get(admin=request.user)
    if 'male' in request.GET:
        user_profile.gender='Male'
        user_profile.save()
    else:
        user_profile.gender='Female'
        user_profile.save()
    print(1)
    return redirect('dashboard')
        



@login_required(login_url='/login')
def profile(request): 
    user_profile = Profile.objects.get(admin=request.user)
    context={
        'title':'Profile',
        'user_profile':user_profile,
    }
    return render(request, 'root/profile.html',context)
        

def verifyandsubmiturl(request):  
    titletosubmit = request.GET['title'] 
    urltosubmit = urllib.parse.urlsplit(request.GET['url'] )
    urltosubmit = urltosubmit.scheme+"://"+urltosubmit.netloc+urltosubmit.path
    
    print(urltosubmit)
    status_code=requests.get(urltosubmit).status_code 
    reqired_profile=Profile.objects.get(admin=request.user)
    if str(reqired_profile.website) in str(urltosubmit) and status_code==200:
        try:
            print('_______________')
            print(urltosubmit)
            x = UserUrlssRepository.objects.get(submitted_url=urltosubmit)
            print('_______________')
            return JsonResponse({"statusduplicate":1}) 
        except :
            UserUrlssRepository.objects.create(title=titletosubmit,submitted_url=urltosubmit,admin=request.user)
            print(status_code)
            item_saved = UserUrlssRepository.objects.all().order_by('-id')[0] 
            return JsonResponse({"status":status_code,'title':titletosubmit,'submitted_url':urltosubmit,'id':item_saved.id})
    else:
        return JsonResponse({"statuserror":0})


def deleteurlfromrepository(request):
    x=UserUrlssRepository.objects.get(id=request.GET['id']).delete()
    return JsonResponse({"status":1})




def authperclick(request): 
    if request.user.is_authenticated:
        return JsonResponse({"q":'passs'})
    else:
        return JsonResponse({"q":000000})
        







 



