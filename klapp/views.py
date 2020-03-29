from django.shortcuts import render
import pytz
import time
#import netifaces as ni

#ni.ifaddresses('wlp6s0')
#ip = ni.ifaddresses('wlp6s0')[ni.AF_INET][0]['addr']


# Create your views here.

def index(request):
    return render(request,'klapp/index.html',{'date_now': time.ctime()}) #third argument give as json this is for dynamic web page/fetch from db etc
