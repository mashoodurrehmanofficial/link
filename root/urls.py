
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('', index, name='index'),   
    # path('confugureurls/', confugureurls, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('verifyweblinkandsubmit/', verifyweblinkandsubmit, name='verifyweblinkandsubmit'),  
    path('sessioncompleted/', sessioncompleted, name='sessioncompleted'),  
    path('sendemailcode/', sendemailcode, name='sendemailcode'),  
    path('verifysentcode/', verifysentcode, name='verifysentcode'),  
    path('personalinfo/', personalinfo, name='personalinfo'),  
    path('profile/', profile, name='profile'),  
    path('authperclick/', authperclick, name='authperclick'),  
    path('verifyandsubmiturl/', verifyandsubmiturl, name='verifyandsubmiturl'),  
    path('deleteurlfromrepository/', deleteurlfromrepository, name='deleteurlfromrepository'),  
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

