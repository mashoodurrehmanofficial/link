
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [   
    path('', dashboard, name='dashboard'),
    path('grablinks/', dashboard, name='grablinks'),
    path('grablinkspacket/', grablinkspacket, name='grablinkspacket'),
    path('claimtraffic/', claimtraffic, name='claimtraffic'),
    path('configureurls/', configureurls, name='configureurls'), 
    path('statistics/', statistics, name='statistics'), 
    path('testurls/', testurls, name='testurls'),  
    path('registermyvisit/', registermyvisit, name='registermyvisit'),  
    path('claimTank/', claimTank, name='claimTank'),  
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

