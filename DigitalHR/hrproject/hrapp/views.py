from django.shortcuts import render, redirect, reverse
from . models import Enquiry, JobSeeker, AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminzone.models import Notification

# Create your views here.
def index(request):
    nf = Notification.objects.all()
    return render(request, "index.html", {'nf': nf})
def parent(request):
    return render(request, "aparent.html")
def aboutus(request):
    return render(request, "aboutus.html")
def registration(request):
    return render(request, "registration.html")
def login(request):
    return render(request, "login.html")
def contactus(request):
    return render(request, "contactus.html")
def saveenq(request):
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contact = request.POST['contactno']
    email = request.POST['emailaddress']
    enquiry = request.POST['enquirytext']
    enq = Enquiry(name=name, gender=gender, address=address, contactno=contact, emailaddress=email, enquirytext=enquiry)
    enq.save()
    msg = 'Your Enquiry is saved'
    return render(request, "contactus.html", {'msg': msg})
def savereg(request):
    name = request.POST['name']
    gender = request.POST['gender']
    address = request.POST['address']
    contact = request.POST['contactno']
    email = request.POST['emailaddress']
    qualification = request.POST['qualification']
    experience = request.POST['experience']
    keyskills = request.POST['keyskills']
    regdate = datetime.datetime.today()
    js = JobSeeker(name=name, gender=gender, address=address, contactno=contact, emailaddress=email, qualification=qualification, experience=experience, keyskills=keyskills, regdate=regdate)
    js.save()
    msg = 'Your registration is done.'
    return render(request, "registration.html", {'msg': msg})
def validateuser(request):
    userid = request.POST['userid']
    password = request.POST['password']
    msg = 'Massage='
    try:
        obj = AdminLogin.objects.get(userid=userid, password=password)
        if obj is not None:
            request.session['userid'] = userid
            return redirect(reverse("adminzone:adminhome"))
    except ObjectDoesNotExist:
        msg = msg+'Invalid User'
    return render(request, "login.html", {'msg': msg})
