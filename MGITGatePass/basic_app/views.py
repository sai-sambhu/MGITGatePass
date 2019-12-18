from django.shortcuts import render
from basic_app.forms import StudentForm,StudentProfileInfoForm
from basic_app.models import StudentProfileInfo,GatepassRequests,AllGatepassRequests
# Create your views here.


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    return render(request,'basic_app/index.html')



def register(request):
    registered=False
    if request.method=="POST":
        
        user_form=StudentForm(data=request.POST)
        profile_form=StudentProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            print("NAME: "+ user_form.cleaned_data['username'])
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pics_students' in request.FILES:
                profile.profile_pic = request.FILES['profile_pics_students']
            profile.save()    
            
            registered=True
        else:
                print(user_form.errors,profile_form.errors)
    else:
         user_form=StudentForm()
         profile_form = StudentProfileInfoForm()
         

    return render (request,'basic_app/registration.html',
                   {'user_form':user_form,'profile_form':profile_form ,
                    'registered':registered}) 
    
@login_required   
def special(request):
     return HttpResponse("your are logged in")     
    
@login_required   
def user_logout(request):
     logout(request)
     return HttpResponseRedirect(reverse('index'))    

@login_required   
def student(request):
    if request.user.studentprofileinfo.typeof=="Incharge":
         logout(request)
         return HttpResponse("You are not a student") 
    gatePassInfos = GatepassRequests.objects.all()
    status='NotRequested'
    for i in gatePassInfos:
        if i.roll == request.user.studentprofileinfo.roll:
            status=i.status
            break
    
    inchargeinfo = StudentProfileInfo.objects.all()
    
    return render(request,'basic_app/student.html',{'inchargeinfos':inchargeinfo,
                                                    "Status":status})
    pass

@login_required   
def gpValidate(request):
    if request.user.studentprofileinfo.typeof=="Incharge":
         logout(request)
         return HttpResponse("You are not a student")
    if request.method=="POST":
           ReasonForm = request.POST['reason']
           if ReasonForm=="":
                 return HttpResponse("Enter a Reason,You dint enter anything.")
           
           user=GatepassRequests.objects.get_or_create(roll= request.user.studentprofileinfo.roll,
                                                       branch=request.user.studentprofileinfo.branch,
                                                       status="Requested",
                                                       reason=ReasonForm) 
           return HttpResponseRedirect(reverse('student'))       
      
    return HttpResponse("Not Authorised")
    pass


@login_required   
def securityClick(request):
    if request.user.studentprofileinfo.typeof=="Incharge":
         logout(request)
         return HttpResponse("You are not a student")
    if request.method=="POST": 
            GatepassRequests.objects.filter(roll= request.user.studentprofileinfo.roll).update(status='OutOfColloge')
            try:
                user=AllGatepassRequests.objects.get_or_create(roll= request.user.studentprofileinfo.roll,
                                                           branch=request.user.studentprofileinfo.branch,
                                                           status="OutOfColloge",
                                                           reason=GatepassRequests.objects.get(roll=request.user.studentprofileinfo.roll).reason,
                                                          dateTime=datetime.datetime.now())
            except:
                 user=AllGatepassRequests.objects.get_or_create(roll= request.user.studentprofileinfo.roll,
                                                           branch=request.user.studentprofileinfo.branch,
                                                           status="OutOfColloge",
                                                           dateTime=datetime.datetime.now())
                
            return HttpResponseRedirect(reverse('student'))
    
    return HttpResponse("Not Authorised")    
    pass
@login_required   
def incharge(request):
    if request.user.studentprofileinfo.typeof=="Student":
         logout(request)
         return HttpResponse("get lost you fool!! You are not a Incharge")
    gatePassInfos = GatepassRequests.objects.all()
                   
    return render(request,'basic_app/incharge.html',{"gatePassInfos":gatePassInfos})
    pass

@login_required   
def inchargeApprove(request):
    if request.user.studentprofileinfo.typeof=="Student":
         logout(request)
         return HttpResponse("get lost you fool!! You are not a Incharge")
   
    if request.method=="POST":
       rolls = request.POST['roll']
       GatepassRequests.objects.filter(roll=rolls).update(status='Approved')    
       
    
    return HttpResponseRedirect(reverse('incharge'))

@login_required   
def inchargeDispprove(request):
    if request.user.studentprofileinfo.typeof=="Student":
         logout(request)
         return HttpResponse("get lost you fool!! You are not a Incharge")
    
    if request.method=="POST":
       rolls = request.POST['roll']
       GatepassRequests.objects.filter(roll=rolls).update(status='Denied')    
       
    
    return HttpResponseRedirect(reverse('incharge'))

    pass

@login_required   
def disapproveAllStudents(request):
    if request.user.studentprofileinfo.typeof=="Student":
         logout(request)
         return HttpResponse("get lost you fool!! You are not a Incharge")
    if request.method=="POST":
        gatePassInfos = GatepassRequests.objects.all() 
        for i in gatePassInfos:
            GatepassRequests.objects.filter(roll=i.roll,branch=request.user.studentprofileinfo.branch).update(status='Denied')
    return HttpResponseRedirect(reverse('incharge'))        
 
  

def refreshAllStudents(request):
    if request.user.studentprofileinfo.typeof=="Student":
         logout(request)
         return HttpResponse("get lost you fool!! You are not a Incharge")
    if request.method=="POST":
        GatepassRequests.objects.filter(branch=request.user.studentprofileinfo.branch).delete()
        
    return HttpResponseRedirect(reverse('incharge'))   

def user_login(request):
    
           
       if request.method=="POST":
           username=request.POST.get('username')
           password=request.POST.get('password')
           
           user=authenticate(username=username,password=password)
          
           
           
           if user:
               
               if user.is_active:
                   login(request,user)
                   print(user.studentprofileinfo.roll,user.studentprofileinfo.typeof)
                   
                   if user.studentprofileinfo.typeof=="Incharge":
                       
                       print("hi")
                       return HttpResponseRedirect(reverse('incharge'))
                   
                   if user.studentprofileinfo.typeof=="Student":
                       return HttpResponseRedirect(reverse('student'))
                  
                   
               else :
                   return HttpResponse("ACCOUNT NOT ACTIVE")
           else:
               print("someone tried to login and failed")
               print(f'username: {username} and password: {password} ')
               return HttpResponse("invalid login details supplied!!")
       
       return render(request,'basic_app/login.html',{})
               