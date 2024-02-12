from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from hrapp.models import AdminLogin, Enquiry, JobSeeker
from . models import Notification
import datetime

# Create your views here.
def adminhome(request):
    try:
        if request.session['userid']:
            return render(request, "adminhome.html")
    except KeyError:
        return render(request, "login.html")
def jobseekers(request):
    try:
        if request.session['userid']:
            js = JobSeeker.objects.all()
            return render(request, "jobseekers.html",{'js': js})
    except KeyError:
        return render(request, "login.html")
def enquiries(request):
    try:
        if request.session['userid']:
            enq = Enquiry.objects.all()
            return render(request, "enquiries.html",{'enq': enq})
    except KeyError:
        return render(request, "login.html")
def changepassword(request):
    try:
        if request.session['userid']:
            return render(request, "changepassword.html")
    except KeyError:
        return render(request, "login.html")
def logout(request):
    request.session['userid'] = None
    return render(request, "login.html")
def adminchangepwd(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    msg = 'message='
    if newpassword != confirmpassword:
        msg = msg+'New Password and Confirm Password is not match.'
        return render(request, "changepassword.html", {'msg': msg})
    userid = request.session['userid']
    try:
        obj = AdminLogin.objects.get(userid=userid, password=oldpassword)
        if obj is not None:
            ad = AdminLogin(userid=userid, password=newpassword)
            ad.save()
            return redirect('adminzone:logout')
    except ObjectDoesNotExist:
        msg = msg+'Old Password is not matched.'
    return render(request, "changepassword.html", {'msg:': msg})
def add(request):
    notificationtext = request.POST['notificationtext']
    notificationdate = datetime.datetime.today()
    nf = Notification(notificationtext=notificationtext,notificationdate=notificationdate)
    nf.save()
    msg = 'Notification is save'
    return render(request, "adminhome.html", {'msg': msg})